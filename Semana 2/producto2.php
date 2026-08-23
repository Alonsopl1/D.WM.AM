```html
<!DOCTYPE html>
<html lang="es">

<head>
    <title>Bombardino Crocodilo</title>
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
            max-width: 430px;
            height: 430px;

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

            <img src="./fotos/cocodrilo.png"
                 class="imagen-producto"
                 alt="Bombardino Crocodilo">

        </div>


        <!-- INFORMACION -->

        <div class="col-md-7 informacion">

            <h1>
                Bombardino Crocodilo
            </h1>

            <div class="precio">
                $20.990
            </div>


            <p class="descripcion">

                Presentamos a Bombardino Crocodilo,
                uno de nuestros brainrots más reconocidos.

                Tiene la forma de un cocodrilo combinado
                con un avión y puede ser manejado mediante
                control remoto.

                Es rápido, ágil y cuenta con un diseño
                exclusivo que lo convierte en uno de los
                personajes más llamativos de nuestra colección.

            </p>


            <p class="descripcion">

                Bombardino Crocodilo mide aproximadamente
                70 cm de largo y 50 cm de ancho.

                Su peso es de aproximadamente 4,5 kg,
                permitiendo transportarlo con facilidad.

                Su estructura está diseñada con materiales
                resistentes y su disponibilidad es limitada,
                debido al alto costo y complejidad de su
                fabricación.

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
```
