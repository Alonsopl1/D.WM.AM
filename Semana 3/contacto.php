<!DOCTYPE html>
<html lang="es">

<head>
    <title>Contacto</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

    <link rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <style>

        body {
            margin: 0;
            background-color: #f5f5f5;
            font-family: Arial, Helvetica, sans-serif;
        }

        .navbar {
            box-shadow: 0 3px 10px rgba(0,0,0,0.18);
        }

        .contacto {
            min-height: calc(100vh - 56px);
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 60px 20px;
            position: relative;
            overflow: hidden;
        }

        .esquina {
            position: absolute;
            width: 130px;
            height: 130px;

            background: linear-gradient(
                135deg,
                #4e2f1b,
                #8b5a2b
            );
        }

        .izquierda {
            top: 0;
            left: 0;
            border-bottom-right-radius: 100%;
        }

        .derecha {
            bottom: 0;
            right: 0;
            border-top-left-radius: 100%;
        }

        .tarjeta-contacto {
            width: 100%;
            max-width: 650px;

            background-color: white;

            padding: 40px;

            border-radius: 16px;
            border-top: 7px solid #6d4c41;

            box-shadow: 0 5px 18px rgba(0,0,0,0.15);

            position: relative;
            z-index: 2;
        }

        .tarjeta-contacto h1 {
            text-align: center;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .subtitulo {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
        }

        .icono {
            text-align: center;
            font-size: 50px;
            color: #6d4c41;
            margin-bottom: 10px;
        }

        .form-control:focus {
            border-color: #6d4c41;
            box-shadow: 0 0 0 0.2rem rgba(109,76,65,0.15);
        }

        .btn-cafe {
            background-color: #6d4c41;
            color: white;
            border: none;
            padding: 10px 25px;
        }

        .btn-cafe:hover {
            background-color: #4e342e;
            color: white;
        }

        @media(max-width: 600px) {

            .tarjeta-contacto {
                padding: 25px;
            }

            .esquina {
                width: 80px;
                height: 80px;
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

                    <li class="nav-item dropdown">

                        <a class="nav-link dropdown-toggle"
                            href="#"
                            role="button"
                            data-bs-toggle="dropdown">

                            Empresa

                        </a>

                        <ul class="dropdown-menu">

                            <li>
                                <a class="dropdown-item"
                                    href="empresa.php#quienes">

                                    Quienes Somos

                                </a>
                            </li>

                            <li>
                                <a class="dropdown-item"
                                    href="empresa.php#equipo">

                                    Nuestro Equipo

                                </a>
                            </li>

                            <li>
                                <a class="dropdown-item"
                                    href="empresa.php#mision">

                                    Mision

                                </a>
                            </li>

                        </ul>

                    </li>

                    <li class="nav-item">

                        <a class="nav-link"
                            href="productos.php">

                            Productos

                        </a>

                    </li>

                    <li class="nav-item">

                        <a class="nav-link active"
                            href="contacto.php">

                            Contacto

                        </a>

                    </li>

                </ul>

            </div>

        </div>

    </nav>


    <!-- CONTACTO -->

    <section class="contacto">

        <div class="esquina izquierda"></div>
        <div class="esquina derecha"></div>

        <div class="tarjeta-contacto">

            <div class="icono">
                <i class="fa fa-envelope"></i>
            </div>

            <h1>Contáctanos</h1>

            <p class="subtitulo">
                Déjanos tu mensaje y nos pondremos en contacto contigo.
            </p>

            <form action="empresa.php">

                <div class="mb-3">

                    <label for="nombre" class="form-label">
                        Nombre:
                    </label>

                    <input
                        type="text"
                        class="form-control"
                        id="nombre"
                        name="nombre"
                        placeholder="Ingresa tu nombre">

                </div>

                <div class="mb-3">

                    <label for="email" class="form-label">
                        Email:
                    </label>

                    <input
                        type="email"
                        class="form-control"
                        id="email"
                        name="email"
                        placeholder="Ingresa tu email">

                </div>

                <div class="mb-3">

                    <label for="comment" class="form-label">
                        Comentarios:
                    </label>

                    <textarea
                        class="form-control"
                        rows="6"
                        id="comment"
                        name="text"
                        placeholder="Escribe tu mensaje aquí"></textarea>

                </div>

                <div class="text-center">

                    <button
                        type="submit"
                        class="btn btn-cafe">

                        <i class="fa fa-paper-plane"></i>
                        Enviar mensaje

                    </button>

                </div>

            </form>

        </div>

    </section>


    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>

</html>