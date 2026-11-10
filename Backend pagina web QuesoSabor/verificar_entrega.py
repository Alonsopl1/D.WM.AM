"""Prueba manual positiva de administración sobre entorno de pruebas.

Requiere TEST_ADMIN_EMAIL y TEST_ADMIN_PASSWORD en entorno. Nunca los imprime.
El usuario se crea con scripts/seed_admin.py (fuera de API pública).
"""
import os,sys,httpx
from uuid import uuid4
url=os.getenv('API_URL','http://127.0.0.1:8000')
email=os.getenv('TEST_ADMIN_EMAIL','')
password=os.getenv('TEST_ADMIN_PASSWORD','')
if not email or not password:
    raise SystemExit('Establece TEST_ADMIN_EMAIL y TEST_ADMIN_PASSWORD en la terminal; no incluya credenciales en el código.')
r=httpx.post(url+'/api/v1/auth/login',json={'usuario':email,'password':password},timeout=6)
assert r.status_code==200 and r.json()['role']=='admin',r.status_code
h={'Authorization':'Bearer '+r.json()['access_token']}
p={'nombre':'Queso de Prueba Temporal','tipo':'Fresco','leche':'Vaca','precio':999,'imagen':'assets/img/queso-fresco.jpg','destacado':False,'descripcion':'Producto inventado solo para probar CRUD.','stock':2}
create=httpx.post(url+'/api/v1/products',headers=h,json=p,timeout=6)
assert create.status_code==201,create.text
pid=create.json()['id']
update=httpx.put(url+f'/api/v1/products/{pid}',headers=h,json={**p,'precio':1999},timeout=6)
assert update.status_code==200,update.text
read=httpx.get(url+f'/api/v1/products/{pid}',timeout=6)
assert read.status_code==200 and read.json()['precio']==1999,read.text
delete=httpx.delete(url+f'/api/v1/products/{pid}',headers=h,timeout=6)
assert delete.status_code==200,delete.text
not_found=httpx.get(url+f'/api/v1/products/{pid}',timeout=6)
assert not_found.status_code==404,not_found.text
print('ADMIN CRUD: PASS (creó, actualizó, consultó y dio de baja un producto temporal).')
tag=uuid4().hex[:12]
client_email=f'checkout-{tag}@example.test'
client_password='ClaveSeguraParaPrueba2026!'
registered=httpx.post(url+'/api/v1/auth/register',json={'nombre':'Cliente Temporal','correo':client_email,'password':client_password},timeout=6)
assert registered.status_code==201,registered.text
login=httpx.post(url+'/api/v1/auth/login',json={'usuario':client_email,'password':client_password},timeout=6)
assert login.status_code==200,login.text
client={'Authorization':'Bearer '+login.json()['access_token']}
order=httpx.post(url+'/api/v1/orders',headers=client,json={'items':[{'product_id':1,'quantity':1}],'idempotency_key':'admin-smoke-'+tag},timeout=6)
assert order.status_code==201,order.text
orderid=order.json()['id']
payment=httpx.post(url+'/api/v1/payments',headers=client,json={'order_id':orderid},timeout=6)
assert payment.status_code==201,payment.text
paymentid=payment.json()['id']
assert httpx.post(url+f'/api/v1/sandbox/payments/{paymentid}/approve',headers=client,timeout=6).status_code==403
approved=httpx.post(url+f'/api/v1/sandbox/payments/{paymentid}/approve',headers=h,timeout=6)
assert approved.status_code==200 and approved.json()['status']=='approved',approved.text
again=httpx.post(url+f'/api/v1/sandbox/payments/{paymentid}/approve',headers=h,timeout=6)
assert again.status_code==200 and again.json()['idempotent'] is True,again.text
paid=httpx.get(url+f'/api/v1/orders/{orderid}',headers=client,timeout=6)
assert paid.status_code==200 and paid.json()['status']=='paid',paid.text
assert httpx.post(url+f'/api/v1/orders/{orderid}/cancel',headers=client,timeout=6).status_code==409
print('ADMIN PAGO SANDBOX: PASS (cliente no puede aprobar; administrador sí; actualización paid e idempotencia).')
