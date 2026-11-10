Servicio;Gateway;Verbo;Ruta externa;Acceso;Destino;Ruta interna;Controles;Credencial simbólica
S01;externo;GET;/api/v1/products;anónimo;inventory;/products;"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-INVENTORY
S02;externo;GET;/api/v1/products/{id};anónimo;inventory;/products/{id};"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-INVENTORY
S03;externo;POST;/api/v1/auth/register;anónimo;auth;/register;"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-AUTH
S04;externo;POST;/api/v1/auth/login;anónimo;auth;/login;"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-AUTH
S05;externo;GET;/api/v1/clients/me;cliente/admin;clients;/me;"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-CLIENTS
S06;externo;PUT;/api/v1/clients/me;cliente/admin;clients;/me;"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-CLIENTS
S07;externo;GET;/api/v1/favorites;cliente/admin;clients;/favorites;"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-CLIENTS
S08;externo;POST;/api/v1/favorites;cliente/admin;clients;/favorites;"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-CLIENTS
S09;externo;DELETE;/api/v1/favorites/{id};cliente/admin;clients;/favorites/{id};"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-CLIENTS
S10;externo;POST;/api/v1/contact;anónimo;clients;/contact;"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-CLIENTS
S11;externo;POST;/api/v1/feedback;anónimo;clients;/feedback;"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-CLIENTS
S12;externo;POST;/api/v1/orders;cliente/admin;orders;/orders;"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-ORDERS
S13;externo;GET;/api/v1/orders;cliente/admin;orders;/orders;"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-ORDERS
S14;externo;GET;/api/v1/orders/{id};cliente/admin;orders;/orders/{id};"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-ORDERS
S15;externo;POST;/api/v1/orders/{id}/cancel;cliente/admin;orders;/orders/{id}/cancel;"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-ORDERS
S16;externo;POST;/api/v1/payments;cliente/admin;payments;/payments;"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-PAYMENTS
S17;externo;GET;/api/v1/payments/{id};cliente/admin;payments;/payments/{id};"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-PAYMENTS
S18;externo;POST;/api/v1/products;admin;inventory;/products;"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-INVENTORY
S19;externo;PUT;/api/v1/products/{id};admin;inventory;/products/{id};"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-INVENTORY
S20;externo;DELETE;/api/v1/products/{id};admin;inventory;/products/{id};"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-INVENTORY
S21;externo;GET;/api/v1/admin/messages;admin;clients;/admin/messages;"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-CLIENTS
S22;externo;POST;/api/v1/sandbox/payments/{id}/approve;admin;payments;/sandbox/payments/{id}/approve;"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-PAYMENTS
S23;externo;POST;/graphql;cliente/admin;graphql;/graphql;"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-GRAPHQL
S24;externo;POST;/graphql;cliente/admin;graphql;/graphql;"JWT/rol/recurso; limit 120/min; max body 32 KiB / GraphQL 8 KiB";REF-GRAPHQL
INT01;interno;POST;NO publicada;solo payments;orders;/internal/orders/{id}/paid;ORDERS_SERVICE_KEY y PAYMENT_CONFIRMATION_KEY, timeout y estado;REF-ORDERS + REF-PAYMENT-CONFIRMATION
