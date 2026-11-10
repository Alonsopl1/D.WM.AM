"""Provisiona credenciales aleatorias para desarrollo LOCAL y archivos Docker secrets.

No imprimir claves. No subir .env ni secrets/ al repositorio.
"""
import secrets
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TARGET=ROOT/'.env'
DIRECTORY=ROOT/'secrets'
NAMES=['JWT_SIGNING_KEY','GATEWAY_CONTEXT_KEY','INVENTORY_SERVICE_KEY',
       'ORDERS_SERVICE_KEY','CLIENTS_SERVICE_KEY','PAYMENTS_SERVICE_KEY',
       'AUTH_SERVICE_KEY','GRAPHQL_SERVICE_KEY','PAYMENT_CONFIRMATION_KEY']

def main():
    existing={}
    if TARGET.exists():
        for line in TARGET.read_text(encoding='utf8').splitlines():
            if '=' in line and not line.lstrip().startswith('#'):
                k,v=line.split('=',1)
                existing[k]=v
    for key in NAMES:
        if len(existing.get(key,''))<32 or existing[key]=='REEMPLAZAR':
            existing[key]=secrets.token_hex(32)
    existing.setdefault('ENABLE_SANDBOX_PAYMENTS','1')
    TARGET.write_text('\n'.join(f'{k}={v}' for k,v in existing.items())+'\n',encoding='utf8')
    DIRECTORY.mkdir(parents=True, exist_ok=True)
    for key in NAMES:
        (DIRECTORY/key).write_text(existing[key]+'\n',encoding='utf8')
        try:(DIRECTORY/key).chmod(0o600)
        except OSError:pass
    try:TARGET.chmod(0o600)
    except OSError:pass
    print('Credenciales locales y archivos Docker secrets preparados (contenido no mostrado).')

if __name__=='__main__':main()
