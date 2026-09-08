const User = require("../models/User");
const Product = require("../models/Product");

const resolvers = {

    Query: {

        getUsers: async () => {
            return await User.find();
        },

        getUser: async (_, { id }) => {
            return await User.findById(id);
        },

        getProducts: async (
            _,
            {
                tipoQueso,
                tipoLeche,
                precioMin,
                precioMax,
                ordenarPor
            }
        ) => {

            const filtro = {};

            if (tipoQueso) {
                filtro.tipoQueso = tipoQueso;
            }

            if (tipoLeche) {
                filtro.tipoLeche = tipoLeche;
            }

            if (precioMin !== undefined || precioMax !== undefined) {

                filtro.precio = {};

                if (precioMin !== undefined) {
                    filtro.precio.$gte = precioMin;
                }

                if (precioMax !== undefined) {
                    filtro.precio.$lte = precioMax;
                }
            }

            let consulta = Product.find(filtro);

            if (ordenarPor === "precioAsc") {
                consulta = consulta.sort({ precio: 1 });
            }

            if (ordenarPor === "precioDesc") {
                consulta = consulta.sort({ precio: -1 });
            }

            if (ordenarPor === "masVendido") {
                consulta = consulta.sort({ masVendido: -1 });
            }

            return await consulta;
        },

        getProduct: async (_, { id }) => {
            return await Product.findById(id);
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
        },

        addProduct: async (_, { input }) => {

            const nuevoProducto = new Product(input);

            return await nuevoProducto.save();
        },

        updateProduct: async (_, { id, input }) => {

            return await Product.findByIdAndUpdate(
                id,
                input,
                {
                    new: true,
                    runValidators: true
                }
            );
        },

        deleteProduct: async (_, { id }) => {
            return await Product.findByIdAndDelete(id);
        }

    }

};

module.exports = resolvers;