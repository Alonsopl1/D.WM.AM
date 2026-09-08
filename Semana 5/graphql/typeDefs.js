const typeDefs = `#graphql

    type User {
        id: ID!
        nombre: String!
        correo: String!
        password: String!
    }

    input UserInput {
        nombre: String!
        correo: String!
        password: String!
    }

    input UserUpdateInput {
        nombre: String
        correo: String
        password: String
    }


    type Product {
        id: ID!
        nombre: String!
        descripcion: String
        precio: Float!
        stock: Int!
        tipoQueso: String!
        tipoLeche: String!
        imagen: String
        masVendido: Boolean!
    }

    input ProductInput {
        nombre: String!
        descripcion: String
        precio: Float!
        stock: Int!
        tipoQueso: String!
        tipoLeche: String!
        imagen: String
        masVendido: Boolean
    }

    input ProductUpdateInput {
        nombre: String
        descripcion: String
        precio: Float
        stock: Int
        tipoQueso: String
        tipoLeche: String
        imagen: String
        masVendido: Boolean
    }


    type Query {

        getUsers: [User]
        getUser(id: ID!): User

        getProducts(
            tipoQueso: String
            tipoLeche: String
            precioMin: Float
            precioMax: Float
            ordenarPor: String
        ): [Product]

        getProduct(id: ID!): Product
    }


    type Mutation {

        addUser(input: UserInput!): User
        updateUser(id: ID!, input: UserUpdateInput!): User
        deleteUser(id: ID!): User

        addProduct(input: ProductInput!): Product
        updateProduct(id: ID!, input: ProductUpdateInput!): Product
        deleteProduct(id: ID!): Product
    }

`;

module.exports = typeDefs;