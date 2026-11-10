# Queso & Sabor · Evaluación 2 — Backend seguro

**Integrantes:** Alonso Pailamilla y Moisés Pacheco.

El backend utiliza los **15 quesos, nombres, precios y categorías** del catálogo de la web responsiva (archivo `frontend/js/productos.js`). Los datos de semilla están en `seed/products.json`. Las pantallas del frontend se adjuntan como referencia del caso, pero no están conectadas a las APIs en esta entrega.

## Componentes

- `gateway`: entrada HTTP única con rutas permitidas, JWT, políticas de roles, rate limit básico, timeout y código de correlación.
- `auth`: login y registro; emite JWT de 30 minutos.
- `inventory`: catálogo, filtros, CRUD administrativo, stock y reserva atómica idempotente.
- `clients`: clientes, contraseñas scrypt con sal, perfiles, favoritos, contacto y comentarios.
- `orders`: validación de precios desde inventory, pedidos persistentes, cancelación, trazabilidad y control por propietario.
- `payments`: pago de **prueba**, persistencia e idempotencia. Simulación de aprobación **solo por administrador**.
- `graphql`: GraphQL privado con campos `resumenPedido` (orders + inventory) y `misFavoritos` (clients + inventory); limita introspección, profundidad, complejidad y consultas no autorizadas.

**Alcance:** los pagos son simulados y no realizan movimientos bancarios. La aplicación frontend no consume las APIs; se incluyen sus datos y operaciones como punto de partida. La decisión sobre analítica y gRPC está fundamentada en `docs/ADR_analitica_grpc.md`.

## Opción A: ejecutar en Windows (VS Code)

**Requisito:** Python 3.11 o superior instalado. Si prefieres evitar la terminal, abre `iniciar_backend_windows.bat` con doble clic; instala dependencias, genera secretos si faltan y arranca los servicios. Abre luego `http://127.0.0.1:8000/api/v1/products?limit=100` en el navegador para ver el catálogo. Para detener, Ctrl+C en la ventana que está ejecutando los servicios.


Abre una terminal en esta carpeta `backend` y ejecuta:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python scripts/make_env.py
python scripts/run_local.py
```

Abre otra terminal con el entorno activo, en la misma carpeta, para las pruebas. Puedes acceder a `http://127.0.0.1:8000/docs`, pero como el gateway utiliza un enrutador por lista blanca, esa página no enumera todas las rutas específicas. Para probarlas cómodamente importa `docs/QuesoSabor.postman_collection.json` en Postman, o utiliza PowerShell/curl. Para terminar usa **Ctrl+C** en la terminal del servidor.

Si PowerShell no permite activar el entorno virtual, usa CMD y `.venv\Scripts\activate.bat`; también puedes llamar directamente `.venv\Scripts\python.exe` sin activarlo.

**Crear administrador de prueba:** Después de iniciar el backend al menos una vez, abre otra terminal y ejecuta `python scripts/seed_admin.py` (ingresa correo/contraseña). Luego inicia sesión en `/api/v1/auth/login`. El registro HTTP normal solo puede crear usuarios `cliente`, nunca administradores.

## Opción B: ejecutar con Docker (mejor aislamiento)

En esta carpeta:

```bash
python scripts/make_env.py
docker compose up --build -d
docker compose ps
docker compose logs gateway
docker compose down
```

El único puerto publicado al host es `127.0.0.1:8000`; `inventory`, `orders`, `clients`, `payments`, `auth` y `graphql` pertenecen a una red Docker privada. Cada dominio almacena su información en un volumen SQLite propio. Para crear un administrador privado dentro de Docker: `docker compose exec -it clients python scripts/seed_admin.py`. Ingrese correo y contraseña en la terminal, nunca en archivos públicos. Nunca habilite el registro público como administrador.

## Flujo práctico sin frontend

1. `GET /api/v1/products?limit=100` → catálogo real de 15 quesos.
2. `POST /api/v1/auth/register` con `{"nombre":"Ana","correo":"ana@example.test","password":"ClaveSegura!2026"}`.
3. `POST /api/v1/auth/login` con `{"usuario":"ana@example.test","password":"ClaveSegura!2026"}` → `access_token`.
4. Agrega `Authorization: Bearer <token>` al consultar favoritos, crear pedidos o pagar.
5. `POST /api/v1/orders` con `{"items":[{"product_id":1,"quantity":2}],"idempotency_key":"compra-demo-0001"}`. El servidor calcula el total desde inventory y reserva el stock.
6. `POST /api/v1/payments` con `{"order_id":"ID_DEL_PEDIDO"}`. Crea pago de prueba `pending`.
7. Un administrador de pruebas puede llamar `POST /api/v1/sandbox/payments/{id}/approve`. No se puede aprobar como cliente.
8. `POST /graphql` con `{ "query": "query($id: ID!) { resumenPedido(id:$id) { id total status items { quantity nombre producto { nombre precio } } } }", "variables": { "id": "ID_DEL_PEDIDO" } }` usando el Bearer del propietario del pedido.

No pongas datos personales verdaderos en las pruebas o en las capturas.

## Pruebas y carga

Con los servicios funcionando:

```bash
python -m pytest -q tests
python scripts/load_test.py --n 40 --workers 4 --out docs/evidencia_carga.json
```

Las 17 pruebas (en cinco archivos) incluyen tests HTTP, verificación de protección por recurso y documentación; las pruebas funcionales realizan altas de usuarios ficticios y pedidos; **modifican la base de datos de prueba**, así que evita ejecutarlos en producción. El resultado y el entorno deben anotarse en la matriz de evidencias.

**Credenciales:** `scripts/make_env.py` prepara 9 secretos aleatorios diferentes (JWT, contexto, seis claves por servicio y una capacidad exclusiva para confirmación de pagos). Para ejecución local permanecen en `.env` (ignorado por Git). Para despliegue con Compose se montan como archivos privados desde `secrets/` usando el mecanismo Docker Compose secrets; las credenciales NO se inyectan como texto en las variables de entorno de los contenedores. Los archivos secretos son secretos locales de laboratorio, no equivalen a Vault, a rotación automática o a un servicio central de producción. Los dos destinos que confirman pagos (`orders` y `payments`) reciben una clave exclusiva que el gateway no conoce. La carpeta `secrets/` está excluida del ZIP y debe crearse en cada PC ejecutando el script. En producción corresponde usar un gestor centralizado y TLS adecuado. Dentro de Compose hay una red privada; eso no sustituye TLS para acceso externo real. Para revocar sesiones en este prototipo se rota la clave JWT (revoca todas) o se espera el vencimiento de 30 min; la revocación individual requiere una lista de revocación para producción.

**Límites declarados:** SQLite y rate limit en memoria son adecuados para la demostración local, no para alta concurrencia distribuida. Los pedidos usan compensación para reponer stock ante fallos, sin transacciones distribuidas; incidencias entre confirmación de cancelación y actualización del pedido requieren reconciliación operacional en producción. GraphQL requiere `graphql-core` del archivo requirements y conexión a sus dependencias en la instalación inicial.

Documentación detallada, matrices, decisiones y diagramas editables se encuentran en `docs/` y el informe adjunto.

## Contratos y anexos

- `docs/01_servicios_y_trazabilidad.csv`: inventario S01–S24. `docs/ejemplos_contratos.json`: 24 ejemplos de petición y respuesta con datos ficticios.
- `docs/02_cardinalidades.csv`, `03_sistemas.csv`, `04_roles_permisos.csv` (72 decisiones rol/servicio), `04_stakeholders.csv` (9 actores), `05_rutas.csv`, `06_secretos.csv` y `07_clasificacion_datos.csv`: matrices de los módulos.
- `docs/schema.graphql`: esquema de dos agregaciones privadas.
- `docs/diagramas/*.drawio`: diagramas UML, componentes y secuencia editables en diagrams.net; `c4_*.dot` y `modelo_c4_structurizr.dsl`: diagramas C4 de contexto C1, contenedores C2 y componentes C3.
- `docs/ADR_analitica_grpc.md`: justifica por qué el caso no necesita gRPC ni analítica separada.
- `docs/evidencia_pruebas.txt` y `docs/evidencia_carga.json`: resultados de pruebas locales.
- `../informe/Informe_Evaluacion_2_Queso_y_Sabor.docx` (y versión PDF): informe de arquitectura y evidencias.

**GraphQL:** el motor estándar es `graphql-core` instalado mediante requirements.txt. El archivo `services/graphql/fallback.py` es un respaldo acotado que permite demostrar las dos Queries sin red para instalar paquetes; no admite todas las características del estándar y no se utiliza como sustituto de graphql-core en producción.

## Arquitectura y pruebas de componentes

Se incluyen modelos de contexto, contenedores y componentes (`docs/diagramas/`), así como tests de autenticación, permisos de recursos, comunicación entre servicios, GraphQL, pedidos e idempotencia. Los tests de `tests/` se pueden ejecutar con el backend iniciado:

```bash
python -m pytest -q tests
```

La clave de idempotencia de un pedido permite repetir de manera segura una solicitud idéntica. Reutilizarla con productos o cantidades diferentes genera HTTP 409. El cliente no puede determinar el precio ni el estado oficial del pago.

`python scripts/verificar_entrega.py` comprueba la cobertura de documentación y permite identificar si están disponibles la dependencia `graphql-core` y Docker. Con Docker Desktop, ejecutar `python scripts/make_env.py`, `docker compose config`, `docker compose up --build -d` y `docker compose ps`. Al terminar, `docker compose down`. Las pruebas previas con GraphQL se ejecutaron en modo de respaldo y Docker está configurado, pero aún requiere comprobación en el equipo donde se vaya a demostrar.

Los ejemplos JSON usan credenciales y tokens ficticios. No emplear datos personales reales en la ejecución de pruebas ni publicar secretos generados localmente.
