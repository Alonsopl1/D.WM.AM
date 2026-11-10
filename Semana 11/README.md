# PR semanal — modelo C4 de Queso & Sabor

## Objetivo

Modelar la arquitectura del proyecto **Queso & Sabor** siguiendo la misma presentación que la referencia de clase: contexto C1, contenedores C2, componentes C3 (API Gateway, GraphQL, Auth y Orders). Los títulos, roles, colores y relaciones están adaptados al proyecto, no copiados de *Natural Power*.

**Esta entrega es documentación de arquitectura.** No crea ni sustituye el backend de la Evaluación 2 ni constituye prueba de implementación de cada elemento mostrado.

## Archivos

- `workspace.dsl`: modelo **editable** en Structurizr DSL, que define las seis vistas, sus entidades y sus relaciones.
- `diagramas/*.png`: los seis gráficos para entregar o incluir en un informe.
- `diagramas/*.svg`: las mismas seis vistas en formato vectorial.
- `diagramas/*.dot`: fuente editable de las representaciones Graphviz.

## Qué representan las vistas

| Vista | Contenido |
| --- | --- |
| `C1_Contexto` | Visitante, cliente, administrador y plataforma Queso & Sabor |
| `C2_Contenedores` | Frontend, gateway, GraphQL, Auth, Inventory, Orders, Clients, Payments, y 5 bases SQLite |
| `C3_Gateway` | Adaptador HTTP, filtro de acceso, despachador de rutas, traductor de errores |
| `C3_GraphQL` | Política por campos, resolvers, conectores, compositor de respuestas |
| `C3_Auth` | Sesiones, verificación de credenciales, repositorio, configuración local de secretos |
| `C3_Orders` | Autorización, idempotencia, lógica de pedidos, adaptadores y repositorio |

## Diferencias importantes respecto del ejemplo de Natural Power

- **Queso & Sabor usa Python/FastAPI**, no Node.js como indica el otro proyecto.
- **Los pagos están simulados en local:** no presentar Webpay o Flow como integraciones ya implementadas.
- **Los secretos se cargan desde entorno/.env**: no presentar Secret Manager remoto ni rotación dinámica como si existieran.
- **No afirmar que GraphQL ya maneja correctamente todos los fallos parciales**: se describe como mejora pendiente.
- **No presentar el frontend como conectado automáticamente al backend**: la documentación describe la separación y las rutas previstas.
- Los componentes C3 son una descripción **lógica** de responsabilidades, no necesariamente módulos independientes ya existentes.

## Cómo abrir en Visual Studio Code

1. Abrir la carpeta raíz del repositorio del equipo.
2. Colocar `arquitectura/` en dicha raíz. Abrir `arquitectura/workspace.dsl` para editar el modelo.
3. Para ver el modelo original en Structurizr, copiar `workspace.dsl` en [Structurizr Playground](https://playground.structurizr.com/) o usar la aplicación local de Structurizr.
4. Abrir los PNG o SVG en VS Code; los `.dot` pueden editarse en texto y regenerarse con Graphviz (`dot -Tpng archivo.dot -o archivo.png`).

**Transparencia técnica:** los PNG/SVG incluidos se dibujaron con **Graphviz** utilizando las mismas entidades y relaciones del modelo C4, ajustando el estilo para parecerse a las capturas de la clase (fondo negro, diagramas verdes y contornos de sistema/contenedor). No son exportaciones nativas de Structurizr. En este entorno no se pudo descargar o ejecutar el validador oficial del DSL, por lo que conviene abrirlo en Structurizr antes de entregar.

## Organización de la entrega en equipo

Consultar `GUIA_COMMITS.md`: primer commit, el modelo DSL; segundo commit, los seis gráficos. Esta división es una propuesta útil de colaboración; la consigna hablada del PR semanal no quedó transcrita de manera verificable.
