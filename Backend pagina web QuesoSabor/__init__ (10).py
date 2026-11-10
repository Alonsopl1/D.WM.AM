from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
from common.base import require_service
from common.transport import call,relay_failure
from common.security import create_access_token

app=FastAPI(title="Queso & Sabor | auth",docs_url=None)
class Login(BaseModel):
    usuario:str=Field(min_length=3)
    password:str=Field(min_length=1)

@app.get('/health')
def health():return {"status":"ok","service":"auth"}

@app.post('/login')
def login(data:Login,request:Request):
    require_service(request,'auth')
    r=call('clients','POST','/auth/verify',json=data.model_dump())
    if r.status_code!=200:relay_failure(r)
    return {"access_token":create_access_token(r.json()),"token_type":"bearer","expires_in":1800,"role":r.json()['role']}

@app.post('/register',status_code=201)
def register(data:dict,request:Request):
    require_service(request,'auth')
    r=call('clients','POST','/auth/register',json=data)
    if r.status_code!=201:relay_failure(r)
    return r.json()
