const mongoose = require("mongoose");

const productSchema = new mongoose.Schema({
    nombre: {
        type: String,
        required: true
    },

    descripcion: {
        type: String
    },

    precio: {
        type: Number,
        required: true
    },

    stock: {
        type: Number,
        required: true,
        default: 0
    },

    tipoQueso: {
        type: String,
        required: true
    },

    tipoLeche: {
        type: String,
        required: true
    },

    imagen: {
        type: String
    },

    masVendido: {
        type: Boolean,
        default: false
    }
});

module.exports = mongoose.model("Product", productSchema);