# Contrato externo publicado en POST /graphql (ejecutado por un servicio PRIVADO)
type Producto { id: Int!, nombre: String!, tipo: String!, leche: String!, precio: Int!, destacado: Boolean!, disponible: Boolean! }
type PedidoLinea { product_id: Int!, quantity: Int!, unit_price: Int!, nombre: String!, producto: Producto }
type PedidoResumen { id: ID!, total: Int!, status: String!, created_at: String!, items: [PedidoLinea!]! }
type Query {
  resumenPedido(id: ID!): PedidoResumen
  misFavoritos: [Producto!]!
}
