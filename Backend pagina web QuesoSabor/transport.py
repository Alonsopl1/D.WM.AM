"""Utilidades compartidas; cada microservicio conserva SU base de datos."""
import os
import sqlite3
from pathlib import Path
from fastapi import HTTPException, Request
import jwt

ROOT = Path(__file__).resolve().parents[1]

def env_secret(name: str) -> str:
    """Resuelve secretos: archivo montado (_FILE) en Compose o variable en modo local.

    No registra el contenido; nunca recibe credenciales del navegador.
    """
    secret_file = os.getenv(name + "_FILE", "")
    if secret_file:
        try:
            value = Path(secret_file).read_text(encoding="utf-8").strip()
        except OSError as exc:
            raise RuntimeError(f"No es posible leer el archivo protegido de {name}") from exc
    else:
        value = os.getenv(name, "")
    if not value or value == "REEMPLAZAR" or len(value) < 32:
        raise RuntimeError(f"Falta secreto seguro: {name}")
    return value

def connect(name: str):
    folder = Path(os.getenv("DATA_DIR", str(ROOT / "data")))
    folder.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(str(folder / (name + ".db")), timeout=10, isolation_level=None)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys=ON")
    con.execute("PRAGMA busy_timeout=5000")
    con.execute("PRAGMA journal_mode=WAL")
    return con

def require_service(request: Request, target: str) -> None:
    import hmac
    actual = request.headers.get("x-service-key", "")
    expected = env_secret(target.upper() + "_SERVICE_KEY")
    if not actual or not hmac.compare_digest(actual, expected):
        raise HTTPException(status_code=403, detail="Servicio interno no autorizado")

def user_context(request: Request, required=True):
    raw = request.headers.get("x-verified-user", "")
    if not raw:
        if required:
            raise HTTPException(401, "Se requiere sesión válida")
        return None
    try:
        decoded = jwt.decode(raw, env_secret("GATEWAY_CONTEXT_KEY"), algorithms=["HS256"], audience="internal")
        if decoded.get("role") not in ("cliente", "admin"):
            raise ValueError("rol no admitido")
        return decoded
    except Exception:
        raise HTTPException(401, "Identidad interna inválida")

def require_admin(user):
    if user["role"] != "admin":
        raise HTTPException(403, "Operación exclusiva de administración")

def public_product(row):
    return {"id":row["id"], "nombre":row["name"], "tipo":row["kind"], "leche":row["milk"],
            "precio":row["price"],"imagen":row["image"],"destacado":bool(row["featured"]),
            "descripcion":row["description"],"disponible":bool(row["active"] and row["stock"]>0)}
