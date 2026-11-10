import sqlite3
from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
from common.base import connect, require_service, user_context, require_admin
from common.security import password_hash, verify_password
from common.transport import call

# EmailStr requeriría email-validator: usamos validación portable con patrón estricto básico.
from pydantic import field_validator

app=FastAPI(title="Queso & Sabor | clients", docs_url=None)

class Register(BaseModel):
    nombre:str=Field(min_length=2,max_length=100)
    correo:str=Field(min_length=5,max_length=200)
    password:str=Field(min_length=10,max_length=128)
    @field_validator('correo')
    @classmethod
    def email_check(cls,v):
        if '@' not in v or '.' not in v.split('@')[-1] or ' ' in v:raise ValueError('Correo inválido')
        return v.lower().strip()

class Credentials(BaseModel):
    usuario:str
    password:str

class Contact(BaseModel):
    nombre:str=Field(min_length=2,max_length=100)
    correo:str=Field(min_length=5,max_length=200)
    asunto:str=Field(min_length=2,max_length=150)
    mensaje:str=Field(min_length=10,max_length=2000)

class Feedback(BaseModel):
    correo:str=Field(min_length=5,max_length=200)
    comentario:str=Field(min_length=8,max_length=2000)

class Favorite(BaseModel):
    product_id:int=Field(gt=0)

class Profile(BaseModel):
    nombre:str=Field(min_length=2,max_length=100)

@app.on_event("startup")
def startup():
    with connect("clients") as db:
        db.execute("""CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT NOT NULL UNIQUE,
          password_hash TEXT NOT NULL,role TEXT NOT NULL DEFAULT 'cliente' CHECK(role IN ('cliente','admin')),
          created_at TEXT NOT NULL)""")
        db.execute("CREATE TABLE IF NOT EXISTS favorites(user_id INTEGER NOT NULL,product_id INTEGER NOT NULL,PRIMARY KEY(user_id,product_id),FOREIGN KEY(user_id) REFERENCES users(id))")
        db.execute("CREATE TABLE IF NOT EXISTS messages(id INTEGER PRIMARY KEY,kind TEXT NOT NULL,name TEXT,email TEXT NOT NULL,subject TEXT,body TEXT NOT NULL,created_at TEXT NOT NULL)")

@app.get("/health")
def health():return {"status":"ok","service":"clients"}

@app.post("/auth/register",status_code=201)
def register(data:Register,request:Request):
    require_service(request,"clients")
    now=datetime.now(timezone.utc).isoformat()
    try:
        with connect("clients") as db:
            cur=db.execute("INSERT INTO users(name,email,password_hash,role,created_at) VALUES(?,?,?,'cliente',?)",(data.nombre.strip(),data.correo,password_hash(data.password),now))
            return {"id":cur.lastrowid,"nombre":data.nombre,"correo":data.correo,"role":"cliente"}
    except sqlite3.IntegrityError:raise HTTPException(409,"Correo ya registrado")

@app.post("/auth/verify")
def verify(data:Credentials,request:Request):
    require_service(request,"clients")
    with connect("clients") as db:
        row=db.execute("SELECT * FROM users WHERE email=?",(data.usuario.lower().strip(),)).fetchone()
    if not row or not verify_password(data.password,row["password_hash"]):raise HTTPException(401,"Credenciales inválidas")
    return {"id":row["id"],"role":row["role"],"nombre":row["name"]}

@app.get("/me")
def me(request:Request):
    require_service(request,"clients");user=user_context(request)
    with connect("clients") as db:
        row=db.execute("SELECT id,name,email,role,created_at FROM users WHERE id=?",(int(user["sub"]),)).fetchone()
    if not row: raise HTTPException(404,"Usuario no encontrado")
    return dict(row)

@app.put("/me")
def update_me(data:Profile,request:Request):
    require_service(request,"clients");user=user_context(request)
    with connect("clients") as db:
        db.execute("UPDATE users SET name=? WHERE id=?",(data.nombre.strip(),int(user["sub"])))
    return {"updated":True}

@app.get("/favorites")
def favorites(request:Request):
    require_service(request,"clients");user=user_context(request)
    with connect("clients") as db:
        ids=[r[0] for r in db.execute("SELECT product_id FROM favorites WHERE user_id=? ORDER BY product_id",(int(user["sub"]),)).fetchall()]
    return {"product_ids":ids}

@app.post("/favorites",status_code=201)
def add_favorite(data:Favorite,request:Request):
    require_service(request,"clients");user=user_context(request)
    p=call("inventory","GET",f"/products/{data.product_id}")
    if p.status_code!=200:raise HTTPException(404,"Producto inexistente")
    with connect("clients") as db:
        db.execute("INSERT OR IGNORE INTO favorites VALUES(?,?)",(int(user["sub"]),data.product_id))
    return {"product_id":data.product_id,"saved":True}

@app.delete("/favorites/{product_id}")
def remove_favorite(product_id:int,request:Request):
    require_service(request,"clients");user=user_context(request)
    with connect("clients") as db:db.execute("DELETE FROM favorites WHERE user_id=? AND product_id=?",(int(user["sub"]),product_id))
    return {"product_id":product_id,"removed":True}

@app.post("/contact",status_code=201)
def contact(data:Contact,request:Request):
    require_service(request,"clients")
    with connect("clients") as db:
        cur=db.execute("INSERT INTO messages(kind,name,email,subject,body,created_at) VALUES('contact',?,?,?,?,?)",(data.nombre.strip(),data.correo.strip(),data.asunto.strip(),data.mensaje.strip(),datetime.now(timezone.utc).isoformat()))
    return {"id":cur.lastrowid,"received":True}

@app.post("/feedback",status_code=201)
def feedback(data:Feedback,request:Request):
    require_service(request,"clients")
    with connect("clients") as db:
        cur=db.execute("INSERT INTO messages(kind,email,body,created_at) VALUES('feedback',?,?,?)",(data.correo.strip(),data.comentario.strip(),datetime.now(timezone.utc).isoformat()))
    return {"id":cur.lastrowid,"received":True}

@app.get("/admin/messages")
def admin_messages(request:Request):
    require_service(request,"clients");require_admin(user_context(request))
    with connect("clients") as db:
        rows=db.execute("SELECT id,kind,name,email,subject,body,created_at FROM messages ORDER BY id DESC LIMIT 100").fetchall()
    return {"items":[dict(r) for r in rows]}
