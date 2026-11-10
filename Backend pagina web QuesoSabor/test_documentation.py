"""Punto de entrada público. Allowlist estricta: no proxy genérico."""
from collections import defaultdict,deque
import re
import time
from uuid import uuid4
from fastapi import FastAPI,Request,HTTPException
from fastapi.responses import JSONResponse
from common.base import env_secret
from common.transport import call
from common.security import decode_access_token,create_internal_token

app=FastAPI(title='Queso & Sabor | API Gateway',version='1.0.0')

# (método, expresión regular, servicio, prefijo interno, acceso)
ROUTES=[
 ('GET',r'/products','inventory','/products','public'),
 ('GET',r'/products/[0-9]+','inventory',None,'public'),
 ('POST',r'/products','inventory',None,'admin'),
 ('PUT',r'/products/[0-9]+','inventory',None,'admin'),
 ('DELETE',r'/products/[0-9]+','inventory',None,'admin'),
 ('POST',r'/auth/login','auth','/login','public'),
 ('POST',r'/auth/register','auth','/register','public'),
 ('GET',r'/clients/me','clients','/me','user'),
 ('PUT',r'/clients/me','clients','/me','user'),
 ('GET',r'/favorites','clients',None,'user'),
 ('POST',r'/favorites','clients',None,'user'),
 ('DELETE',r'/favorites/[0-9]+','clients',None,'user'),
 ('GET',r'/orders','orders',None,'user'),
 ('POST',r'/orders','orders',None,'user'),
 ('GET',r'/orders/[a-f0-9]{32}','orders',None,'user'),
 ('POST',r'/orders/[a-f0-9]{32}/cancel','orders',None,'user'),
 ('POST',r'/payments','payments',None,'user'),
 ('GET',r'/payments/[a-f0-9]{32}','payments',None,'user'),
 ('POST',r'/sandbox/payments/[a-f0-9]{32}/approve','payments',None,'admin'),
 ('POST',r'/contact','clients',None,'public'),
 ('POST',r'/feedback','clients',None,'public'),
 ('GET',r'/admin/messages','clients',None,'admin'),
]
_windows=defaultdict(deque)

@app.get('/health')
def health():return {'status':'ok','service':'gateway'}

def _identity(request,access):
    header=request.headers.get('authorization','')
    if not header:
        if access=='public':return None
        raise HTTPException(401,'Se requiere Bearer token')
    if not header.startswith('Bearer '):raise HTTPException(401,'Autenticación inválida')
    try:user=decode_access_token(header[7:])
    except Exception:raise HTTPException(401,'Sesión inválida o expirada')
    if access=='admin' and user.get('role')!='admin':raise HTTPException(403,'Permiso insuficiente')
    return user

def _limit(request):
    # Básico para demostración; producción multinodo requiere almacén compartido (Redis).
    ip=request.client.host if request.client else 'unknown'
    now=time.monotonic();window=_windows[ip]
    while window and window[0]<now-60:window.popleft()
    if len(window)>=120:raise HTTPException(429,'Límite de solicitudes alcanzado')
    window.append(now)

@app.post('/graphql')
async def graphql(request:Request):
    _limit(request)
    user=_identity(request,'user')
    raw=await request.body()
    if len(raw)>8192:raise HTTPException(413,'Consulta demasiado grande')
    try:payload=await request.json()
    except Exception:raise HTTPException(400,'JSON inválido')
    context=create_internal_token(user)
    r=call('graphql','POST','/graphql',context=context,json=payload)
    try:body=r.json()
    except ValueError:raise HTTPException(502,'Respuesta interna inválida')
    return JSONResponse(body,status_code=r.status_code,headers={'X-Request-ID':uuid4().hex})

@app.api_route('/api/v1/{path:path}',methods=['GET','POST','PUT','DELETE'])
async def public_api(path:str,request:Request):
    _limit(request)
    route='/'+path
    match=next((r for r in ROUTES if r[0]==request.method and re.fullmatch(r[1],route)),None)
    if not match:raise HTTPException(404,'Ruta o verbo no disponible')
    _,_,destination,rewrite,access=match
    user=_identity(request,access)
    internal_context=create_internal_token(user) if user else None
    raw=await request.body()
    if len(raw)>32768:raise HTTPException(413,'Cuerpo demasiado grande')
    data=None
    if raw:
        try:data=await request.json()
        except ValueError:raise HTTPException(400,'JSON inválido')
    target=rewrite if rewrite else route
    query=dict(request.query_params)
    r=call(destination,request.method,target,context=internal_context,params=query,json=data)
    try:body=r.json()
    except ValueError:body={'detail':'Respuesta del servicio no disponible'}
    return JSONResponse(body,status_code=r.status_code,headers={'X-Request-ID':uuid4().hex})
