"""Ejecuta los siete servicios para una demostración en localhost (sin frontend)."""
import os,sys,subprocess,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.chdir(ROOT)
dotenv=ROOT/'.env'
if not dotenv.exists():
    raise SystemExit('Falta .env. Primero ejecuta: python scripts/make_env.py')
env=os.environ.copy()
for line in dotenv.read_text(encoding='utf8').splitlines():
    if '=' in line and not line.startswith('#'):
        k,v=line.split('=',1);env[k]=v
services=[('auth',8101),('inventory',8102),('clients',8103),('orders',8104),('payments',8105),('graphql',8106),('gateway',8000)]
if '--no-graphql' in sys.argv:services=[x for x in services if x[0]!='graphql']
processes=[]
try:
    for service,port in services:
        command=[sys.executable,'-m','uvicorn',f'services.{service}.app:app','--host','127.0.0.1','--port',str(port),'--no-access-log']
        p=subprocess.Popen(command,cwd=str(ROOT),env=env)
        processes.append(p)
        print(f'{service:10s}: http://127.0.0.1:{port}',flush=True)
    print('\nAPI exterior: http://127.0.0.1:8000/docs\nDetener: CTRL+C',flush=True)
    while all(p.poll() is None for p in processes):time.sleep(0.3)
    print('Se detuvo uno de los servicios; revisar mensajes anteriores.')
except KeyboardInterrupt:pass
finally:
    for p in processes:p.terminate()
    for p in processes:
        try:p.wait(timeout=5)
        except subprocess.TimeoutExpired:p.kill()
