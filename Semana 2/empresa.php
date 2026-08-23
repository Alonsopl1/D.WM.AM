<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Empresa</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

    <link rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <style>

        body {
            margin: 0;
            background-color: #f5f5f5;
        }

        .contenedor-tarjetas {
            display: flex;
            justify-content: center;
            align-items: stretch;
            gap: 35px;

            max-width: 1200px;
            margin: 60px auto;
            padding: 20px;
        }

        .tarjeta {
            width: 300px;
            min-height: 480px;

            background-color: white;

            border: 1px solid #d6d6d6;
            border-radius: 12px;

            padding: 30px;

            box-shadow: 0px 4px 15px rgba(0,0,0,0.12);

            display: flex;
            flex-direction: column;
        }

        .tarjeta h2 {
            text-align: center;
            font-size: 26px;
            margin-bottom: 15px;
        }

        .tarjeta hr {
            width: 100%;
            margin-bottom: 25px;
        }

        .tarjeta p {
            font-size: 16px;
            line-height: 1.6;
            text-align: justify;
        }

        @media (max-width: 900px) {

            .contenedor-tarjetas {
                flex-direction: column;
                align-items: center;
            }

            .tarjeta {
                width: 90%;
                min-height: 350px;
            }

        }

    </style>

</head>

<body>

    <!-- NAVBAR -->

    <nav class="navbar navbar-expand-sm bg-dark navbar-dark">

        <div class="container-fluid">

            <a class="navbar-brand" href="index.php">
                <i class="fa fa-car"></i>
            </a>

            <button class="navbar-toggler"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#collapsibleNavbar">

                <span class="navbar-toggler-icon"></span>

            </button>

            <div class="collapse navbar-collapse" id="collapsibleNavbar">

                <ul class="navbar-nav">

                    <!-- EMPRESA -->

                    <li class="nav-item dropdown">

                        <a class="nav-link dropdown-toggle"
                            href="#"
                            role="button"
                            data-bs-toggle="dropdown">

                            Empresa

                        </a>

                        <ul class="dropdown-menu">

                            <li>
                                <a class="dropdown-item" href="#quienes">
                                    Quienes Somos
                                </a>
                            </li>

                            <li>
                                <a class="dropdown-item" href="#equipo">
                                    Nuestro Equipo
                                </a>
                            </li>

                            <li>
                                <a class="dropdown-item" href="#mision">
                                    Mision
                                </a>
                            </li>

                        </ul>

                    </li>

                    <!-- PRODUCTOS -->

                    <li class="nav-item">

                        <a class="nav-link" href="productos.php">
                            Productos
                        </a>

                    </li>

                    <!-- CONTACTO -->

                    <li class="nav-item">

                        <a class="nav-link" href="contacto.php">
                            Contacto
                        </a>

                    </li>

                </ul>

            </div>

        </div>

    </nav>


    <!-- CUADROS -->

    <div class="contenedor-tarjetas">

        <!-- QUIENES SOMOS -->

        <div class="tarjeta" id="quienes">

            <h2>Quienes Somos</h2>

            <hr>

            <p>
                Somos una empresa dedicada a entregar productos
                usando componentes de primera calidad y con un equipo
                comprometido que quiere que nuestro trabajo llegue
                a todos los rincones del mundo, entregando un servicio
                de alta calidad.
            </p>

        </div>


        <!-- NUESTRO EQUIPO -->

        <div class="tarjeta" id="equipo">

            <h2>Nuestro Equipo</h2>

            <hr>

            <p>
                Nuestro equipo está compuesto por dos personas,
                Moises y Alonso, comprometidas con esta causa.

                Queremos entregar la mayor satisfacción a nuestros
                clientes y que se sientan parte de nuestra familia,
                dándole la mayor importancia a sus necesidades.
            </p>

        </div>


        <!-- MISION -->

        <div class="tarjeta" id="mision">

            <h2>Mision</h2>

            <hr>

            <p>
                Nuestra misión es proporcionar brainrots de calidad,
                con la mayor exclusividad y la mejor calidad de
                productos que una empresa pueda ofrecer a sus clientes.

                Buscamos la satisfacción absoluta al adquirir
                nuestros productos.
            </p>

        </div>

    </div>


    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>

</html>