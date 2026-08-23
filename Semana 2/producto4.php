<!DOCTYPE html>
<html lang="es">

<head>
    <title>Tralalero Tralala</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
          rel="stylesheet">

    <style>

        body {
            margin: 0;
            background-color: #f5f5f5;
            font-family: Arial, Helvetica, sans-serif;
        }

        .producto-detalle {
            max-width: 1100px;
            margin: 60px auto;
            background-color: white;
            padding: 40px;
            border-radius: 16px;
            border-top: 7px solid #6d4c41;
            box-shadow: 0 5px 18px rgba(0,0,0,0.15);
        }

        .contenedor-imagen {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .imagen-producto {
            width: 100%;
            max-width: 420px;
            height: 420px;
            object-fit: contain;
            background-color: #eeeeee;
            border-radius: 12px;
            padding: 10px;
        }

        .informacion {
            padding: 20px 30px;
        }

        .informacion h1 {
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .precio {
            font-size: 30px;
            font-weight: bold;
            color: #6d4c41;
            margin-bottom: 25px;
        }

        .descripcion {
            font-size: 16px;
            line-height: 1.7;
            color: #444;
            text-align: justify;
            margin-bottom: 25px;
        }

        .btn-cafe {
            background-color: #6d4c41;
            color: white;
            border: none;
            padding: 11px 22px;
        }

        .btn-cafe:hover {
            background-color: #4e342e;
            color: white;
        }

        @media(max-width: 768px) {
            .producto-detalle {
                margin: 20px;
                padding: 20px;
            }

            .imagen-producto {
                max-width: 350px;
                height: 350px;
            }

            .informacion {
                padding: 30px 5px 5px;
            }
        }

    </style>

</head>

<body>

<div class="producto-detalle">

    <div class="row align-items-center">

        <!-- IMAGEN -->
        <div class="col-md-5 contenedor-imagen">

            <img src="./fotos/tralalero.png"
                 class="imagen-producto"
                 alt="Tralalero Tralala">

        </div>

        <!-- INFORMACION -->
        <div class="col-md-7 informacion">

            <h1>
                Tralalero Tralala
            </h1>

            <div class="precio">
                $30.990
            </div>

            <p class="descripcion">
                Nuestro cuarto y último producto, llamado
                Tralalero Tralala, es un brainrot elaborado
                completamente a mano, con un diseño exclusivo
                y único en todo el mundo.

                Existen solamente 10 unidades y cada una fue
                fabricada por un reconocido diseñador de brainrots
                llamado Benjamin Andres.
            </p>

            <p class="descripcion">
                Tralalero Tralala mide aproximadamente
                65 cm de alto y 45 cm de ancho.

                Su peso es de 3,5 kg, lo que lo convierte
                en un brainrot liviano y fácil de transportar.

                Su disponibilidad es extremadamente limitada,
                ya que solo se fabricaron 10 unidades de este
                modelo exclusivo.
            </p>

            <a href="productos.php"
               class="btn btn-cafe">

                Volver a productos

            </a>

        </div>

    </div>

</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>

</html>