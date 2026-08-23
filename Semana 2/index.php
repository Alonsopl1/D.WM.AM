<!DOCTYPE html>
<html lang="es">

<head>
    <title>Mi Empresa</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

    <link rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <style>

        body {
            background-color: #f5f5f5;
        }

        .navbar {
            box-shadow: 0 3px 10px rgba(0,0,0,0.2);
        }

        .btn-cafe {
            background-color: #6d4c41;
            color: white;
            border: none;
        }

        .btn-cafe:hover {
            background-color: #4e342e;
            color: white;
        }

        .portada {
            text-align: center;
            padding: 80px 20px;
            background-color: white;
            position: relative;
            overflow: hidden;
        }

        .portada h1 {
            font-size: 45px;
            font-weight: bold;
        }

        .portada p {
            font-size: 18px;
            color: #666;
            max-width: 700px;
            margin: 20px auto;
        }

        .esquina {
            position: absolute;
            width: 130px;
            height: 130px;
            background: linear-gradient(135deg, #4e2f1b, #8b5a2b);
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

        .seccion {
            padding: 60px 20px;
        }

        .tarjeta {
            background-color: white;
            padding: 30px;
            border-radius: 15px;
            border-top: 6px solid #6d4c41;
            box-shadow: 0 4px 15px rgba(0,0,0,0.12);
            text-align: center;
            height: 100%;
        }

        .tarjeta i {
            font-size: 50px;
            color: #6d4c41;
            margin-bottom: 15px;
        }

        .tarjeta p {
            color: #666;
        }

    </style>

</head>

<body>

<nav class="navbar navbar-expand-sm bg-dark navbar-dark">

    <div class="container-fluid">

        <a class="navbar-brand" href="index.php">
            <i class="fa fa-car"></i>
        </a>

        <button class="navbar-toggler"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#menu">

            <span class="navbar-toggler-icon"></span>

        </button>

        <div class="collapse navbar-collapse" id="menu">

            <ul class="navbar-nav">

                <li class="nav-item dropdown">

                    <a class="nav-link dropdown-toggle"
                       href="#"
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

                    <a class="nav-link"
                       href="contacto.php">

                        Contacto

                    </a>

                </li>

            </ul>

        </div>

        <button class="btn btn-cafe"
                data-bs-toggle="modal"
                data-bs-target="#myModal">

            Acceder

        </button>

    </div>

</nav>


<div class="portada">

    <div class="esquina izquierda"></div>
    <div class="esquina derecha"></div>

    <h1>
        Bienvenido a Nuestra Tienda
    </h1>

    <p>
        Descubre nuestros productos exclusivos,
        elaborados y seleccionados pensando
        en entregar calidad a nuestros clientes.
    </p>

    <a href="productos.php"
       class="btn btn-cafe btn-lg">

        Ver Productos

    </a>

</div>


<div class="container seccion">

    <h2 class="text-center mb-5">
        Conoce Nuestra Página
    </h2>

    <div class="row g-4">

        <div class="col-md-4">

            <div class="tarjeta">

                <i class="fa fa-building"></i>

                <h3>
                    Nuestra Empresa
                </h3>

                <p>
                    Conoce quiénes somos,
                    nuestro equipo y nuestra misión.
                </p>

                <a href="empresa.php"
                   class="btn btn-cafe">

                    Conocer más

                </a>

            </div>

        </div>


        <div class="col-md-4">

            <div class="tarjeta">

                <i class="fa fa-shopping-bag"></i>

                <h3>
                    Productos
                </h3>

                <p>
                    Revisa nuestros productos,
                    precios y características.
                </p>

                <a href="productos.php"
                   class="btn btn-cafe">

                    Ver productos

                </a>

            </div>

        </div>


        <div class="col-md-4">

            <div class="tarjeta">

                <i class="fa fa-envelope"></i>

                <h3>
                    Contacto
                </h3>

                <p>
                    ¿Tienes dudas?
                    Puedes comunicarte con nosotros.
                </p>

                <a href="contacto.php"
                   class="btn btn-cafe">

                    Contactarnos

                </a>

            </div>

        </div>

    </div>

</div>


<div class="modal fade" id="myModal">

    <div class="modal-dialog">

        <div class="modal-content">

            <div class="modal-header">

                <h4 class="modal-title">
                    Autenticación
                </h4>

                <button type="button"
                        class="btn-close"
                        data-bs-dismiss="modal">
                </button>

            </div>

            <div class="modal-body">

                <form action="empresa.php">

                    <div class="mb-3">

                        <label class="form-label">
                            Email:
                        </label>

                        <input type="email"
                               class="form-control"
                               placeholder="Ingresa tu email">

                    </div>

                    <div class="mb-3">

                        <label class="form-label">
                            Contraseña:
                        </label>

                        <input type="password"
                               class="form-control"
                               placeholder="Ingresa tu contraseña">

                    </div>

                    <button type="submit"
                            class="btn btn-cafe">

                        Iniciar sesión

                    </button>

                </form>

            </div>

        </div>

    </div>

</div>

</body>

</html>