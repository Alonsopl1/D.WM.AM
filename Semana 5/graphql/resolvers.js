const User = require("../models/User");

const resolvers = {

    Query: {

        getUsers: async () => {
            return await User.find();
        },

        getUser: async (_, { id }) => {
            return await User.findById(id);
        }

    },

    Mutation: {

        addUser: async (_, { input }) => {

            const nuevoUsuario = new User({
                nombre: input.nombre,
                correo: input.correo,
                password: input.password
            });

            return await nuevoUsuario.save();
        },

        updateUser: async (_, { id, input }) => {

            return await User.findByIdAndUpdate(
                id,
                input,
                {
                    new: true
                }
            );
        },

        deleteUser: async (_, { id }) => {

            return await User.findByIdAndDelete(id);

        }

    }

};

module.exports = resolvers;