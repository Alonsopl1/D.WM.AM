"""Crea cuenta admin de desarrollo en clients.db; no se publica por API."""
import os,sys,getpass,sqlite3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from common.base import connect
from common.security import password_hash
from datetime import datetime,timezone

email=input('Correo del administrador: ').strip().lower()
password=getpass.getpass('Contraseña (mínimo 10 caracteres): ')
if len(password)<10 or '@' not in email:raise SystemExit('Correo/contraseña inválidos')
try:
    with connect('clients') as db:
        db.execute("INSERT INTO users(name,email,password_hash,role,created_at) VALUES(?, ?, ?, 'admin', ?)",('Administrador',email,password_hash(password),datetime.now(timezone.utc).isoformat()))
    print('Administrador de prueba creado.')
except sqlite3.IntegrityError:print('Ya existe cuenta con ese correo; sin cambios.')
except sqlite3.OperationalError:print('Primero ejecuta al menos una vez clients para crear la tabla users.')
