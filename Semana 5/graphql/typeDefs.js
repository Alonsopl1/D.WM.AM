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

    type Query {
        getUsers: [User]
        getUser(id: ID!): User
    }

    type Mutation {
        addUser(input: UserInput!): User
        updateUser(id: ID!, input: UserUpdateInput!): User
        deleteUser(id: ID!): User
    }

`;

module.exports = typeDefs;