"""Preflight reproducible de E2. No instala paquetes, no expone secretos."""
from __future__ import annotations
from pathlib import Path
import csv, importlib.util, json, shutil

ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'

def main():
    with (DOCS/'01_servicios_y_trazabilidad.csv').open(encoding='utf-8-sig',newline='') as f:
        ids={r['ID'] for r in csv.DictReader(f,delimiter=';')}
    with (DOCS/'04_roles_permisos.csv').open(encoding='utf-8-sig',newline='') as f:
        permits=list(csv.DictReader(f,delimiter=';'))
    examples=json.loads((DOCS/'ejemplos_contratos.json').read_text(encoding='utf-8'))['contratos']
    ex_ids={v['id'] for v in examples}
    expected={(role,i) for role in ('Visitante','Cliente','Administrador') for i in ids}
    actual={(x['Rol / identidad'],x['ID de servicio']) for x in permits}
    results={
        '24_servicios':len(ids)==24,
        '24_contratos_json':ex_ids==ids and len(examples)==24,
        '72_rol_servicio':actual==expected and len(permits)==72,
        'existe_uml_editable':bool(list((DOCS/'diagramas').glob('*.drawio'))),
        'existe_schema_graphql':(DOCS/'schema.graphql').exists(),
        'existe_compose':(ROOT/'compose.yaml').exists(),
    }
    print('EVALUACIÓN 2 · COMPROBACIONES ESTÁTICAS')
    for name,ok in results.items():print(('OK' if ok else 'FALTA'),name)
    print('graphql-core instalado:', 'SÍ' if importlib.util.find_spec('graphql') is not None else 'NO (solo respaldo acotado)')
    print('Docker disponible:', 'SÍ (ejecutar docker compose config y docker compose up)' if shutil.which('docker') else 'NO (Compose no ejecutado)')
    if shutil.which('docker'):
        print('Docker requiere una ejecución completa antes de afirmar que el despliegue fue probado.')
    print('Los datos de ejemplo son ficticios; no se imprimen secretos.')
    return 0 if all(results.values()) else 1

if __name__=='__main__':raise SystemExit(main())
