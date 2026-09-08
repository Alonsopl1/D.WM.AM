require("dotenv").config();

const mongoose = require("mongoose");

const { ApolloServer } = require("@apollo/server");
const {
    startStandaloneServer
} = require("@apollo/server/standalone");

const typeDefs = require("./graphql/typeDefs");
const resolvers = require("./graphql/resolvers");


async function iniciarServidor() {

    try {

        // Conectar con MongoDB
        await mongoose.connect(process.env.MONGO_URI);

        console.log("MongoDB conectado correctamente");

        // Crear servidor GraphQL
        const server = new ApolloServer({
            typeDefs,
            resolvers
        });

        // Iniciar servidor
        const { url } = await startStandaloneServer(server, {
            listen: {
                port: 4000
            }
        });

        console.log("Servidor funcionando en:");
        console.log(url);

    } catch (error) {

        console.error("Error al iniciar el servidor:");
        console.error(error);

    }
}


iniciarServidor();