Dato;Finalidad;Clase;Custodio;Roles;Exposición frontend;Protección;Retención
Nombre/descripción/tipo/leche/precio queso;Exhibir catálogo;público;inventory;visitante;tarjeta producto;"validación; no secretos";hasta desactivación lógica
Stock;Control de disponibilidad;interno;inventory;"servicios; admin escribe";solo disponible sí/no;"SQL transaccional; cuenta no pública";mientras producto exista
Nombre/correo cliente;Registro y contacto;personal restringido;clients;propietario/admin;perfil propio;"JWT+propiedad; no loguear";hasta baja/retención justificada
Hash de contraseña con sal;Autenticar;credencial derivada;clients;auth interno verifica;nunca;"scrypt+sal; sin texto plano";hasta cambio/baja
Access token JWT;Sesión temporal;credencial de sesión;auth/gateway;titular;Bearer en cliente;"HS256; caduca 30min";"expira 30min; rotación global"
Pedidos y líneas;Historial de compras;restringido;orders;propietario/admin;historial propio;"JWT/owner check; snapshots";historial comercial justificado
Estado y monto del pago;Verificar compra;restringido;payments;propietario/admin;detalle propio;"backend manda; no confiar en navegador";historial comercial
Formulario de contacto/comentarios;Recibir consultas;personal restringido;clients;admin;se envía al backend;"max longitud; acceso admin";definir política de retención
Claves API interservicio;Integración;secreto técnico;Docker secrets; .env solo local;solo servicios;nunca;"archivos secretos montados por servicio; gitignore";rotación al incidente
