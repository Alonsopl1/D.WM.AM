"""Parser GraphQL acotado para demostraciones sin graphql-core.

NO es motor GraphQL general: soporta exclusivamente dos consultas Query
existentes, variables ID!, selección de campos y límites estrictos.
Para cumplimiento completo del estándar instalar graphql-core (requirements.txt).
"""
import re
from fastapi import HTTPException

FIELDS = {
    'Query': {'resumenPedido': 'PedidoResumen', 'misFavoritos': 'Producto'},
    'PedidoResumen': {'id': None, 'total': None, 'status': None, 'created_at': None, 'items': 'PedidoLinea'},
    'PedidoLinea': {'product_id': None, 'quantity': None, 'unit_price': None, 'nombre': None, 'producto': 'Producto'},
    'Producto': {'id': None, 'nombre': None, 'tipo': None, 'leche': None, 'precio': None, 'destacado': None, 'disponible': None},
}
TOKEN = re.compile(r'\s+|#[^\n]*|\.{3}|[!$():{},\[\]]|[A-Za-z_][\w]*|\d+|"(?:\\.|[^"\\])*"')

class Parser:
    def __init__(self, query):
        if len(query) > 4000: raise HTTPException(413, 'Consulta demasiado larga')
        self.tokens = []
        idx=0
        for m in TOKEN.finditer(query):
            if m.start()!=idx: raise HTTPException(400, 'Token GraphQL inválido')
            idx=m.end()
            if not m.group().isspace() and not m.group().startswith('#'):
                self.tokens.append(m.group())
        if idx!=len(query): raise HTTPException(400, 'Token GraphQL inválido')
        self.pos=0
        self.cost=0
    def peek(self):
        return self.tokens[self.pos] if self.pos<len(self.tokens) else None
    def take(self, expected=None):
        v=self.peek()
        if v is None or (expected is not None and v!=expected):
            raise HTTPException(400, f'Sintaxis GraphQL: se esperaba {expected or "valor"}')
        self.pos+=1
        return v
    def name(self):
        v=self.take()
        if not re.fullmatch(r'[A-Za-z_]\w*',v):raise HTTPException(400,'Se esperaba identificador')
        if v.startswith('__'):raise HTTPException(403,'Introspección no habilitada')
        return v
    def parse(self):
        variables=set()
        if self.peek()=='query':
            self.take()
            if self.peek()!='{' and self.peek()!='(':
                self.name() # nombre de operación
            if self.peek()=='(':
                self.take('(')
                while self.peek()!=')':
                    self.take('$');variable=self.name();self.take(':')
                    self.take('ID');self.take('!');variables.add(variable)
                    if self.peek()==',':self.take(',')
                self.take(')')
        selection=self.selection('Query',1)
        if self.peek() is not None:raise HTTPException(400,'Solo una operación Query sin fragmentos')
        return selection, variables
    def selection(self,kind,depth):
        if depth>5:raise HTTPException(400,'Profundidad GraphQL excedida')
        self.take('{')
        fields={}
        while self.peek()!='}':
            if self.peek() is None:raise HTTPException(400,'Llaves sin cerrar')
            self.cost+=1
            if self.cost>30:raise HTTPException(400,'Costo GraphQL excedido')
            name=self.name()
            if name not in FIELDS[kind]:raise HTTPException(400,'Campo GraphQL no autorizado')
            if name in fields:raise HTTPException(400,'Campo repetido')
            arg=None
            if self.peek()=='(':
                if kind!='Query' or name!='resumenPedido':raise HTTPException(400,'Argumentos no permitidos')
                self.take('(');self.take('id');self.take(':')
                if self.peek()=='$':
                    self.take('$');arg=('variable',self.name())
                else:
                    value=self.take()
                    if not (value.startswith('"') and value.endswith('"')):raise HTTPException(400,'ID inválido')
                    arg=('literal',value[1:-1])
                self.take(')')
            if kind=='Query' and name=='resumenPedido' and arg is None:
                raise HTTPException(400,'Se requiere id para resumenPedido')
            child_kind=FIELDS[kind][name]
            if child_kind:
                if self.peek()!='{':raise HTTPException(400,'Falta selección de subcampos')
                child=self.selection(child_kind,depth+1)
            else:
                if self.peek()=='{':raise HTTPException(400,'Un campo escalar no admite subcampos')
                child=None
            fields[name]=(arg,child)
        self.take('}')
        if not fields:raise HTTPException(400,'Selección vacía')
        return fields

def project(obj, selection):
    if obj is None:return None
    if isinstance(obj,list):return [project(v,selection) for v in obj]
    return {name: project(obj.get(name),child) if child else obj.get(name) for name,(_,child) in selection.items()}

def run(query,variables,resolve_order,resolve_favorites):
    selection,required=Parser(query).parse()
    variables=variables or {}
    if not isinstance(variables,dict):raise HTTPException(400,'Variables no válidas')
    if any(key not in variables or not isinstance(variables[key],str) for key in required):
        raise HTTPException(400,'Variables ID! obligatorias')
    result={}
    for name,(arg,child) in selection.items():
        if name=='resumenPedido':
            value=variables[arg[1]] if arg[0]=='variable' else arg[1]
            source=resolve_order(value)
        else: source=resolve_favorites()
        result[name]=project(source,child)
    return {'data':result}
