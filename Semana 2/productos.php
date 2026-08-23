<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Productos</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background-color: #f5f5f5;
            color: #222;
        }

        .navbar {
            box-shadow: 0 3px 10px rgba(0,0,0,0.18);
        }

        .cabecera {
            text-align: center;
            padding: 45px 20px 30px;
        }

        .cabecera h1 {
            font-size: 38px;
            font-weight: bold;
            margin-bottom: 8px;
        }

        .cabecera p {
            color: #666;
            font-size: 17px;
            margin: 0;
        }

        .productos {
            width: 96%;
            max-width: 1500px;
            margin: 0 auto;
            padding: 20px 0 70px;

            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 24px;
        }

        .producto {
            background-color: white;
            border: 1px solid #dddddd;
            border-top: 7px solid #6d4c41;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.13);

            display: flex;
            flex-direction: column;

            transition: 0.25s;
        }

        .producto:hover {
            transform: translateY(-6px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.20);
        }

        .zona-foto {
            width: 100%;
            height: 300px;
            background-color: #eeeeee;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        .imagen-producto {
            width: 100%;
            height: 100%;
            object-fit: contain;
            padding: 10px;
        }

        .texto-foto {
            color: #888;
            font-size: 15px;
            text-align: center;
            padding: 20px;
        }

        .informacion {
            padding: 22px;
            display: flex;
            flex-direction: column;
            flex: 1;
        }

        .informacion h2 {
            font-size: 22px;
            font-weight: bold;
            text-align: center;
            margin: 0 0 15px;
        }

        .descripcion {
            color: #555;
            font-size: 15px;
            line-height: 1.5;
            text-align: center;
            margin-bottom: 20px;
        }

        .precio {
            color: #6d4c41;
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            margin-top: auto;
            margin-bottom: 18px;
        }

        .boton {
            display: block;
            background-color: #6d4c41;
            color: white;
            text-decoration: none;
            text-align: center;
            padding: 12px;
            border-radius: 7px;
            font-weight: bold;
        }

        .boton:hover {
            background-color: #4e342e;
            color: white;
        }

        @media(max-width: 1100px) {
            .productos {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }
        }

        @media(max-width: 600px) {
            .productos {
                width: 92%;
                grid-template-columns: 1fr;
            }
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
                       role="button"
                       data-bs-toggle="dropdown">
                        Empresa
                    </a>

                    <ul class="dropdown-menu">
                        <li>
                            <a class="dropdown-item" href="empresa.php#quienes">
                                Quienes Somos
                            </a>
                        </li>

                        <li>
                            <a class="dropdown-item" href="empresa.php#equipo">
                                Nuestro Equipo
                            </a>
                        </li>

                        <li>
                            <a class="dropdown-item" href="empresa.php#mision">
                                Mision
                            </a>
                        </li>
                    </ul>
                </li>

                <li class="nav-item">
                    <a class="nav-link active" href="productos.php">
                        Productos
                    </a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="contacto.php">
                        Contacto
                    </a>
                </li>

            </ul>
        </div>
    </div>
</nav>


<div class="cabecera">
    <h1>Nuestros Productos</h1>
    <p>Conoce nuestra colección de figuras exclusivas</p>
</div>


<div class="productos">

    <!-- PRODUCTO 1 -->
    <div class="producto">

        <div class="zona-foto">
            <img src="./fotos/tungtung.png"
             class="imagen-producto"
              alt="Tung Tung Sahur collectible figure displayed on an exhibition stand against a neutral background">
            
            
        </div>

        <div class="informacion">
            <h2>Tung Tung Sahur</h2>

            <p class="descripcion">
                Figura coleccionable de Tung Tung Sahur con base de exhibición.
            </p>

            <p class="precio">$15.990</p>

            <a href="producto1.php" class="boton">
                Ver producto
            </a>
        </div>
    </div>


    <!-- PRODUCTO 2 -->
    <div class="producto">

        <div class="zona-foto">
            <img src="./fotos/cocodrilo.png"
            class="imagen-producto"
            alt="Bombardino Crocodilo">
        </div>

        <div class="informacion">
            <h2>Bombardiro Cocodrillo</h2>

            <p class="descripcion">
                Figura especial de Bombardino Crocodilo con control remoto incluido.
            </p>

            <p class="precio">$20.990</p>

            <a href="producto2.php" class="boton">
                Ver producto
            </a>
        </div>
    </div>


    <!-- PRODUCTO 3 -->
    <div class="producto">

        <div class="zona-foto">
            <img src="./fotos/ballerina.png"
            class="imagen-producto"
            alt="Bailarina Cappuccina">
        </div>

        <div class="informacion">
            <h2>Bailarina Cappuccina</h2>

            <p class="descripcion">
                Figura coleccionable presentada en una elegante vitrina de exhibición.
            </p>

            <p class="precio">$9.990</p>

            <a href="producto3.php" class="boton">
                Ver producto
            </a>
        </div>
    </div>


    <!-- PRODUCTO 4 -->
    <div class="producto">

        <div class="zona-foto">
            <img src="./fotos/tralalero.png"
            class="imagen-producto"
            alt="Tralalero Tralala">
        </div>

        <div class="informacion">
            <h2>Tralalero Tralala</h2>

            <p class="descripcion">
                Figura coleccionable de Tralalera tralala con zapatillas azules incluidas.
            </p>

            <p class="precio">$30.990</p>

            <a href="producto4.php" class="boton">
                Ver producto
            </a>
        </div>
    </div>

</div>


<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>