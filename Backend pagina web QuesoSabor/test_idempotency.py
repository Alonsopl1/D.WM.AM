"""GraphQL privado de verdad (graphql-core), sin acceso directo a bases ajenas."""
from fastapi import FastAPI,Request,HTTPException
from fastapi.responses import JSONResponse
try:
    from graphql import (build_schema,graphql_sync,parse,validate,GraphQLError,OperationDefinitionNode,
                         FieldNode,SelectionSetNode,FragmentDefinitionNode,FragmentSpreadNode,InlineFragmentNode)
    HAS_GRAPHQL_CORE=True
except ModuleNotFoundError:
    HAS_GRAPHQL_CORE=False
    from services.graphql.fallback import run as fallback_run
from common.base import require_service,user_context
from common.transport import call

app=FastAPI(title='Queso & Sabor | GraphQL privado',docs_url=None)
SCHEMA='''
  type Producto { id: Int!, nombre: String!, tipo: String!, leche: String!, precio: Int!, destacado: Boolean!, disponible: Boolean! }
  type PedidoLinea { product_id: Int!, quantity: Int!, unit_price: Int!, nombre: String!, producto: Producto }
  type PedidoResumen { id: ID!, total: Int!, status: String!, created_at: String!, items: [PedidoLinea!]! }
  type Query { resumenPedido(id: ID!): PedidoResumen, misFavoritos: [Producto!]! }
'''
schema=build_schema(SCHEMA) if HAS_GRAPHQL_CORE else None

def order_summary(root,info,id):
    context=info.context['context']
    r=call('orders','GET',f'/orders/{id}',context=context)
    if r.status_code==403:
        if HAS_GRAPHQL_CORE: raise GraphQLError('No está autorizado a consultar ese pedido')
        raise HTTPException(403, 'No está autorizado a consultar ese pedido')
    if r.status_code==404:return None
    if r.status_code!=200:
        if HAS_GRAPHQL_CORE: raise GraphQLError('No se pudo consultar el pedido')
        raise HTTPException(503, 'No se pudo consultar el pedido')
    order=r.json()
    ids=','.join(str(v['product_id']) for v in order['items'])
    products=call('inventory','GET','/products/lookup',params={'ids':ids})
    if products.status_code!=200:
        # No devolver producto=null como si estuviera legítimamente ausente.
        # Un error explicito muestra que se perdió información de inventory.
        if HAS_GRAPHQL_CORE: raise GraphQLError('Catálogo no disponible en este momento')
        raise HTTPException(503,'Catálogo no disponible en este momento')
    mapped={p['id']:p for p in products.json()['items']}
    # Snapshot del pedido permanece disponible aunque el producto sea dado de baja.
    for line in order['items']:line['producto']=mapped.get(line['product_id'])
    return order

def favorites(root,info):
    context=info.context['context']
    r=call('clients','GET','/favorites',context=context)
    if r.status_code!=200:
        if HAS_GRAPHQL_CORE: raise GraphQLError('Error consultando favoritos')
        raise HTTPException(503, 'Error consultando favoritos')
    ids=r.json()['product_ids']
    if not ids:return []
    p=call('inventory','GET','/products/lookup',params={'ids':','.join(map(str,ids))})
    if p.status_code!=200:
        if HAS_GRAPHQL_CORE: raise GraphQLError('Catálogo no disponible')
        raise HTTPException(503, 'Catálogo no disponible')
    return p.json()['items']

if HAS_GRAPHQL_CORE:
    schema.type_map['Query'].fields['resumenPedido'].resolve=order_summary
    schema.type_map['Query'].fields['misFavoritos'].resolve=favorites

@app.get('/health')
def health():return {'status':'ok','service':'graphql'}

def analyze(query:str):
    if not HAS_GRAPHQL_CORE: return None
    if len(query)>4000:raise HTTPException(413,'Consulta GraphQL demasiado extensa')
    try:ast=parse(query)
    except Exception:raise HTTPException(400,'Sintaxis GraphQL inválida')
    if any(isinstance(x,FragmentDefinitionNode) for x in ast.definitions):
        raise HTTPException(400,'Fragments deshabilitados para limitar costo')
    ops=[d for d in ast.definitions if isinstance(d,OperationDefinitionNode)]
    if len(ops)!=1 or ops[0].operation.value!='query':raise HTTPException(400,'Solo se permiten Queries')
    def walk(sel,depth=1):
        count=0
        if depth>5:raise HTTPException(400,'Profundidad GraphQL excedida')
        for item in sel.selections:
            if isinstance(item,(FragmentSpreadNode,InlineFragmentNode)):
                raise HTTPException(400,'Fragments no admitidos')
            if isinstance(item,FieldNode):
                if item.name.value.startswith('__'):raise HTTPException(403,'Introspección no habilitada')
                count+=1
                if item.selection_set:count+=walk(item.selection_set,depth+1)
        return count
    if walk(ops[0].selection_set)>30:raise HTTPException(400,'Costo de consulta excedido')
    errors=validate(schema,ast)
    if errors:raise HTTPException(400,'Campos o argumentos GraphQL inválidos')
    return ast

@app.post('/graphql')
async def graphql(request:Request):
    require_service(request,'graphql');user_context(request)
    payload=await request.json()
    if not isinstance(payload,dict) or not isinstance(payload.get('query'),str):raise HTTPException(400,'Falta query')
    query=payload['query'];analyze(query)
    variables=payload.get('variables')
    if variables is not None and not isinstance(variables,dict):raise HTTPException(400,'Variables inválidas')
    if not HAS_GRAPHQL_CORE:
        # Compatibilidad local/offline de alcance explícitamente limitado.
        return JSONResponse(fallback_run(query,variables,
            lambda id:order_summary(None,type('Info',(),{'context':{'context':request.headers['x-verified-user']}})(),id),
            lambda:favorites(None,type('Info',(),{'context':{'context':request.headers['x-verified-user']}})())))
    result=graphql_sync(schema,query,variable_values=variables,context_value={'context':request.headers['x-verified-user']})
    body={'data':result.data}
    if result.errors:body['errors']=[{'message':e.message if e.message in ('No está autorizado a consultar ese pedido', 'Catálogo no disponible en este momento', 'Catálogo no disponible') else 'Error de ejecución GraphQL'} for e in result.errors]
    return JSONResponse(body)
