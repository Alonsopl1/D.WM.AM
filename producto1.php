<!DOCTYPE html>
<html lang="es">

<head>
    <title>Tung Tung Sahur</title>
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

        /* TARJETA PRINCIPAL */

        .producto-detalle {
            max-width: 1100px;
            margin: 60px auto;
            background-color: white;

            padding: 40px;

            border-radius: 16px;
            border-top: 7px solid #6d4c41;

            box-shadow: 0 5px 18px rgba(0,0,0,0.15);
        }


        /* ZONA DE LA IMAGEN */

        .contenedor-imagen {
            display: flex;
            justify-content: center;
            align-items: center;
        }


        /* IMAGEN */

        .imagen-producto {
            width: 100%;
            max-width: 420px;
            height: 480px;

            object-fit: contain;

            border-radius: 12px;

            background-color: #eeeeee;

            padding: 10px;
        }


        /* INFORMACION */

        .informacion {
            padding: 20px 30px;
        }


        .informacion h1 {
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 10px;
        }


        /* PRECIO */

        .precio {
            font-size: 30px;
            font-weight: bold;

            color: #6d4c41;

            margin-bottom: 25px;
        }


        /* TEXTOS */

        .descripcion {
            font-size: 16px;
            line-height: 1.7;

            color: #444;

            text-align: justify;

            margin-bottom: 25px;
        }


        /* BOTON */

        .btn-cafe {
            background-color: #6d4c41;
            color: white;

            padding: 11px 22px;

            border: none;
        }


        .btn-cafe:hover {
            background-color: #4e342e;
            color: white;
        }


        /* CELULAR */

        @media(max-width: 768px) {

            .producto-detalle {
                margin: 20px;
                padding: 20px;
            }

            .imagen-producto {
                max-width: 350px;
                height: 400px;
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


        <!-- IMAGEN A LA IZQUIERDA -->

        <div class="col-md-5 contenedor-imagen">

            <img src="./fotos/tungtung.png"
                 class="imagen-producto"
                 alt="Tung Tung Sahur">

        </div>



        <!-- INFORMACION A LA DERECHA -->

        <div class="col-md-7 informacion">

            <h1>
                Tung Tung Sahur
            </h1>


            <div class="precio">
                $15.990
            </div>


            <p class="descripcion">

                Nuestro primer producto es conocido mundialmente
                como Tung Tung Tung Sahur. Es uno de los brainrots
                más queridos y recordados.

                Está hecho de una madera de alta calidad y cuenta
                con un diseño característico de nuestra marca,
                convirtiéndolo en una figura única dentro de
                nuestra colección.

            </p>


            <p class="descripcion">

                Tung Tung Tung Sahur mide aproximadamente 67 cm
                de alto y 45 cm de ancho.

                Su peso es de aproximadamente 3,5 kg, lo que
                permite transportarlo fácilmente.

                Su disponibilidad es limitada debido a que su
                fabricación es costosa y su diseño es exclusivo.

            </p>


            <a href="productos.php"
               class="btn btn-cafe">

                Volver a productos

            </a>

        </div>


    </div>

</div>


<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js">
</script>


</body>

</html>