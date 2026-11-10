// Queso & Sabor - Arquitectura C4 (referencia visual de la clase: verde sobre fondo oscuro)
// Código de arquitectura (NO implementa ni modifica el backend operativo).
// Fuente conceptual: servicios del proyecto y elementos vistos en las clases C1/C2/C3.
// IMPORTANTE: El pago es un simulador local; .env no equivale a un gestor externo de secretos.

workspace "Queso & Sabor - Modelo C4" "Contexto, contenedores y componentes de la plataforma comercial" {
    !identifiers hierarchical

    model {
        visitante = person "Visitante" "Explora el catálogo sin autenticarse."
        cliente = person "Cliente" "Consulta productos, administra favoritos y realiza pedidos."
        operador = person "Administrador" "Administra productos y gestiona operaciones autorizadas."

        plataforma = softwareSystem "Queso & Sabor" "Plataforma de catálogo y pedidos de quesos." {
            frontend = container "Frontend responsivo" "Interfaz web de visitantes, clientes y administradores." "HTML, CSS y JavaScript" {
                tags "Web"
            }

            gateway = container "API Gateway" "Entrada HTTP; controles de acceso, despacho de rutas y manejo de errores." "Python / FastAPI" {
                adaptador = component "Adaptador HTTP" "Recibe solicitudes y devuelve respuestas HTTP." "FastAPI"
                filtro = component "Filtro de acceso" "Valida la ruta pública o autenticada y el rol permitido." "Python"
                despachador = component "Despachador de rutas" "Envía cada petición al servicio autorizado." "Python / HTTP"
                errores = component "Traductor de errores" "Normaliza errores para el consumidor y evita divulgar detalles internos." "Python"
            }

            auth = container "Auth Service" "Credenciales, emisión y comprobación de tokens de sesión." "Python / FastAPI" {
                sesiones = component "Gestor de sesiones JWT" "Emite y comprueba tokens con vigencia limitada; sin revocación individual implementada." "Python / JWT"
                credenciales = component "Verificador de credenciales" "Comprueba contraseñas mediante hashes seguros." "Python / scrypt"
                identidades = component "Repositorio de identidades" "Consulta y guarda las credenciales de usuario." "Python / SQLite"
                config = component "Configuración local de secretos" "Carga claves desde variables del entorno; NO es un gestor externo de secretos." ".env / variables de entorno" {
                    tags "AlcanceLimitado"
                }
            }

            graphql = container "GraphQL Gateway" "Agrega datos de pedidos, inventario y clientes para consultas privadas." "Python / GraphQL" {
                politica = component "Política de acceso a campos" "Restringe consultas a campos y recursos autorizados." "Python"
                resolvers = component "Resolvers de negocio" "Construye las respuestas consultando servicios de dominio." "Python / GraphQL"
                conectores = component "Conectores de servicios" "Consulta inventory, orders y clients mediante contratos internos." "Python / HTTP"
                compositor = component "Compositor de respuestas" "En el diseño objetivo debe declarar fallos parciales explícitamente." "Python" {
                    tags "Objetivo"
                }
            }

            inventory = container "inventory" "Mantiene productos, precios y disponibilidad." "Python / FastAPI"
            orders = container "orders" "Crea pedidos y administra sus estados." "Python / FastAPI" {
                autorizacion = component "Política de acceso a pedidos" "Comprueba permisos y pertenencia del pedido." "Python"
                idempotencia = component "Control de idempotencia" "Evita duplicar operaciones al recibir reintentos." "Python"
                negocio = component "Servicio de pedidos" "Aplica reglas de negocio y coordina el pedido." "Python"
                inventario = component "Adaptador de inventario" "Consulta productos y disponibilidad." "Python / HTTP"
                pagos = component "Adaptador de pagos" "Coordina estados de pago con el simulador." "Python / HTTP"
                repositorio = component "Repositorio de pedidos" "Lee y escribe pedidos de la base correspondiente." "Python / SQLite"
            }
            clients = container "clients" "Perfiles de clientes y favoritos." "Python / FastAPI"
            payments = container "payments" "Simulación local de pagos y estados; sin proveedor de pago real." "Python / FastAPI" {
                tags "Simulado"
            }

            db_auth = container "Datos de identidad" "Credenciales e identidades del servicio auth." "SQLite" {

                tags "Database"

            }
            db_inventory = container "Datos de inventario" "Datos persistentes de productos." "SQLite" {
                tags "Database"
            }
            db_orders = container "Datos de pedidos" "Pedidos e información asociada." "SQLite" {
                tags "Database"
            }
            db_clients = container "Datos de clientes" "Perfiles y favoritos." "SQLite" {
                tags "Database"
            }
            db_payments = container "Datos de pagos" "Estados del simulador de pagos." "SQLite" {
                tags "Database"
            }
        }

        // C1: personas y plataforma como sistema completo.
        visitante -> plataforma "Explora el catálogo de quesos"
        cliente -> plataforma "Consulta catálogo, favoritos y pedidos"
        operador -> plataforma "Administra catálogo y operaciones"

        // C2: recorrido general entre contenedores.
        visitante -> plataforma.frontend "Navega sin iniciar sesión" "HTTPS"
        cliente -> plataforma.frontend "Consulta y opera su cuenta" "HTTPS"
        operador -> plataforma.frontend "Administra recursos" "HTTPS"
        plataforma.frontend -> plataforma.gateway "Consume la API" "HTTP/JSON"
        plataforma.gateway -> plataforma.auth "Autenticación y autorización" "HTTP/JSON"
        plataforma.gateway -> plataforma.graphql "Consultas agregadas" "HTTP/GraphQL"
        plataforma.gateway -> plataforma.inventory "Operaciones de catálogo" "HTTP/JSON"
        plataforma.gateway -> plataforma.orders "Operaciones de pedidos" "HTTP/JSON"
        plataforma.gateway -> plataforma.clients "Gestión de clientes" "HTTP/JSON"
        plataforma.gateway -> plataforma.payments "Consulta estados de pago" "HTTP/JSON"
        plataforma.graphql -> plataforma.inventory "Obtiene productos" "HTTP/JSON"
        plataforma.graphql -> plataforma.orders "Obtiene pedidos" "HTTP/JSON"
        plataforma.graphql -> plataforma.clients "Obtiene clientes/favoritos" "HTTP/JSON"
        plataforma.orders -> plataforma.inventory "Consulta disponibilidad" "HTTP/JSON"
        plataforma.orders -> plataforma.payments "Coordina pago simulado" "HTTP/JSON"
        plataforma.auth -> plataforma.db_auth "Lee y escribe" "SQLite"
        plataforma.inventory -> plataforma.db_inventory "Lee y escribe" "SQLite"
        plataforma.orders -> plataforma.db_orders "Lee y escribe" "SQLite"
        plataforma.clients -> plataforma.db_clients "Lee y escribe" "SQLite"
        plataforma.payments -> plataforma.db_payments "Lee y escribe" "SQLite"

        // C3 - API Gateway.
        plataforma.frontend -> plataforma.gateway.adaptador "Envía solicitudes web"
        plataforma.gateway.adaptador -> plataforma.gateway.filtro "Pasa solicitud"
        plataforma.gateway.filtro -> plataforma.gateway.despachador "Permite ruta autorizada"
        plataforma.gateway.filtro -> plataforma.auth "Valida token/rol"
        plataforma.gateway.despachador -> plataforma.graphql "Despacha consultas agregadas"
        plataforma.gateway.despachador -> plataforma.inventory "Despacha catálogo"
        plataforma.gateway.despachador -> plataforma.orders "Despacha pedidos"
        plataforma.gateway.despachador -> plataforma.clients "Despacha clientes"
        plataforma.gateway.despachador -> plataforma.payments "Despacha pagos"
        plataforma.gateway.despachador -> plataforma.gateway.errores "Entrega resultado o error"
        plataforma.gateway.errores -> plataforma.gateway.adaptador "Respuesta consistente"

        // C3 - GraphQL Gateway.
        plataforma.gateway -> plataforma.graphql.politica "Envía consultas GraphQL autorizadas"
        plataforma.graphql.politica -> plataforma.graphql.resolvers "Autoriza operaciones"
        plataforma.graphql.resolvers -> plataforma.graphql.conectores "Solicita datos"
        plataforma.graphql.conectores -> plataforma.inventory "Consulta productos"
        plataforma.graphql.conectores -> plataforma.orders "Consulta pedidos"
        plataforma.graphql.conectores -> plataforma.clients "Consulta favoritos"
        plataforma.graphql.conectores -> plataforma.graphql.compositor "Proporciona resultados o errores"
        plataf orma.graphql.resolvers -> plataforma.graphql.compositor "Compone datos de negocio"

        // C3 - Auth Service.
        plataforma.gateway -> plataforma.auth.sesiones "Solicita validación de sesión"
        plataforma.auth.sesiones -> plataforma.auth.credenciales "Comprueba inicio de sesión"
        plataforma.auth.credenciales -> plataforma.auth.identidades "Consulta identidad"
        plataforma.auth.identidades -> plataforma.db_auth "Lee y escribe identidades"
        plataforma.auth.sesiones -> plataforma.auth.config "Obtiene claves JWT"

        // C3 - orders.
        plataforma.gateway -> plataforma.orders.autorizacion "Envía petición de pedido"
        plataforma.orders.autorizacion -> plataforma.orders.idempotencia "Permite acción y valida reintento"
        plataforma.orders.idempotencia -> plataforma.orders.negocio "Procesa una sola vez"
        plataforma.orders.negocio -> plataforma.orders.inventario "Comprueba disponibilidad"
        plataforma.orders.negocio -> plataforma.orders.pagos "Coordina estado de pago"
        plataforma.orders.negocio -> plataforma.orders.repositorio "Persiste pedido"
        plataforma.orders.inventario -> plataforma.inventory "Consulta producto"
        plataforma.orders.pagos -> plataforma.payments "Gestiona pago de laboratorio"
        plataforma.orders.repositorio -> plataforma.db_orders "Lee y escribe pedidos"
    }

    views {
        systemContext plataforma "C1_Contexto" "Quién usa la plataforma y para qué." {
            include *
            autoLayout lr
        }
        container plataforma "C2_Contenedores" "Qué servicios y datos participan en la solución." {
            include *
            autoLayout lr
        }
        component plataforma.gateway "C3_Gateway" "Componentes internos del API Gateway." {
            include *
            autoLayout lr
        }
        component plataforma.graphql "C3_GraphQL" "Componentes internos del GraphQL Gateway." {
            include *
            autoLayout lr
        }
        component plataforma.auth "C3_Auth" "Componentes internos de autenticación." {
            include *
            autoLayout lr
        }
        component plataforma.orders "C3_Orders" "Componentes internos de pedidos." {
            include *
            autoLayout lr
        }

        styles {
            element "Person" {
                shape Person
                background #207B55
                color #FFFFFF
            }
            element "Software System" {
                shape RoundedBox
                background #2CA06D
                color #FFFFFF
            }
            element "Container" {
                shape RoundedBox
                background #3AB37F
                color #FFFFFF
            }
            element "Component" {
                shape RoundedBox
                background #80D0AA
                color #122D21
            }
            element "Database" {
                shape Cylinder
                background #2EAE80
                color #FFFFFF
            }
            element "Web" {
                background #35A978
                color #FFFFFF
            }
            element "Simulado" {
                background #A87434
                color #FFFFFF
            }
            element "Objetivo" {
                background #A87434
                color #FFFFFF
            }
            element "AlcanceLimitado" {
                background #A87434
                color #FFFFFF
            }
            relationship "Relationship" {
                color #A9B7AF
                thickness 2
            }
        }
    }
}
