<!DOCTYPE html>
<html lang="es">
<head>
    <title>Bombardino Crocodilo</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    
    <style>
        body { margin: 0; background-color: #f5f5f5; font-family: Arial, Helvetica, sans-serif; }
        .navbar { box-shadow: 0 3px 10px rgba(0,0,0,0.18); }
        .producto-detalle { max-width: 1100px; margin: 40px auto; background-color: white; padding: 40px; border-radius: 16px; border-top: 7px solid #6d4c41; box-shadow: 0 5px 18px rgba(0,0,0,0.15); }
        .contenedor-imagen { display: flex; justify-content: center; align-items: center; }
        .imagen-producto { width: 100%; max-width: 420px; height: 420px; object-fit: contain; background-color: #eeeeee; border-radius: 12px; padding: 10px; }
        .informacion { padding: 20px 30px; }
        .informacion h1 { font-size: 36px; font-weight: bold; margin-bottom: 10px; }
        .precio { font-size: 30px; font-weight: bold; color: #6d4c41; margin-bottom: 20px; }
        .descripcion { font-size: 16px; line-height: 1.7; color: #444; text-align: justify; margin-bottom: 22px; }
        .zona-compra { margin-top: 25px; padding: 20px; background-color: #f7f3f1; border-radius: 10px; }
        .cantidad { width: 110px; }
        .stock { margin-top: 10px; margin-bottom: 5px; color: #555; font-weight: bold; }
        .mensaje-stock { min-height: 24px; color: red; font-weight: bold; margin-bottom: 10px; }
        .botones { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 15px; }
        .btn-cafe { background-color: #6d4c41; color: white; border: none; padding: 11px 22px; }
        .btn-cafe:hover { background-color: #4e342e; color: white; }
    </style>

    <script>
        const respuestaAPI = {
            "status": 200,
            "message": "Productos obtenidos correctamente",
            "data": [
                { "id": 1, "nombre": "Tung Tung Sahur", "precio": 15990, "stock": 5 },
                { "id": 2, "nombre": "Bombardino Crocodilo", "precio": 20990, "stock": 3 },
                { "id": 3, "nombre": "Ballerina Cappuccina", "precio": 15990, "stock": 8 },
                { "id": 4, "nombre": "Tralalero Tralala", "precio": 30990, "stock": 10 }
            ]
        };

        respuestaAPI.data.forEach((producto) => {
            console.log(`${producto.nombre} - $${producto.precio}`);
        });

        let variable1 = null;
        console.log(typeof(variable1));
        variable1 = { "rut": "1-9"};
        console.log(typeof(variable1.rut));
        
        let variable2 = NaN;
        console.log(typeof(variable2));
        variable2 = 1/0;
        console.log(typeof(variable2)); console.log(variable2);
        
        variable2 = 1/variable1;
        console.log(typeof(variable2)); console.log(variable2);
        
        let variable3;
        console.log(typeof(variable3));
        console.log(variable3 instanceof Object);
        console.log(null instanceof Object);
        
        try { 
            variable2 = variable2 + y;
        } catch (err) {
            console.log(`Error ${err}`);
        }

        const idProducto = 2; // ID ACTUALIZADO
        let productoActual;

        function cargarProducto() {
            try {
                productoActual = respuestaAPI.data.find(producto => producto.id == idProducto);
                if (productoActual == undefined) throw new Error("Producto no encontrado");

                document.getElementById("nombreProducto").innerText = productoActual.nombre;
                document.getElementById("precioProducto").innerText = "$" + productoActual.precio.toLocaleString("es-CL");
                document.getElementById("stockProducto").innerText = "Stock disponible: " + productoActual.stock;
                
                const contenedorContador = document.getElementById("contenedor-contador");
                contenedorContador.innerHTML = "";

                const labelCantidad = document.createElement("label");
                labelCantidad.setAttribute("for", "cantidad");
                labelCantidad.className = "form-label";
                labelCantidad.innerHTML = "<strong>Cantidad:</strong>";

                const selectCantidad = document.createElement("select");
                selectCantidad.id = "cantidad";
                selectCantidad.className = "form-select cantidad";
                
                if(productoActual.stock === 0) {
                    selectCantidad.disabled = true;
                    document.getElementById("btnAgregar").disabled = true;
                    const opcionVacia = document.createElement("option");
                    opcionVacia.text = "Sin stock";
                    selectCantidad.appendChild(opcionVacia);
                } else {
                    for (let i = 1; i <= productoActual.stock; i++) {
                        const opcion = document.createElement("option");
                        opcion.value = i;
                        opcion.text = i;
                        selectCantidad.appendChild(opcion);
                    }
                }

                contenedorContador.appendChild(labelCantidad);
                contenedorContador.appendChild(selectCantidad);

            } catch (err) {
                console.log(`Error ${err}`);
            }
        }
    </script>
</head>

<body onload="cargarProducto(); actualizarCarrito();">

    <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="index.php"><i class="fa fa-car"></i></a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="collapsibleNavbar">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item"><a class="nav-link active" href="productos.php">Volver a Productos</a></li>
                </ul>
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link text-warning" data-bs-toggle="offcanvas" href="#carritoLateral" role="button">
                            <i class="fa fa-shopping-cart"></i> Carrito (<span id="contador-carrito">0</span>)
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

<div class="producto-detalle">
    <div class="row align-items-center">
        <div class="col-md-5 contenedor-imagen">
            <img src="./fotos/cocodrilo.png" class="imagen-producto" alt="Bombardino Crocodilo">
        </div>

        <div class="col-md-7 informacion">
            <h1 id="nombreProducto">Cargando...</h1>
            <div class="precio" id="precioProducto">$0</div>

            <p class="descripcion">
                Presentamos a Bombardino Crocodilo, uno de nuestros brainrots más reconocidos. Tiene la forma de un cocodrilo combinado con un avión y puede ser manejado mediante control remoto. Es rápido, ágil y cuenta con un diseño exclusivo que lo convierte en uno de los personajes más llamativos de nuestra colección.
            </p>
            <p class="descripcion">
                Bombardino Crocodilo mide aproximadamente 70 cm de largo y 50 cm de ancho. Su peso es de aproximadamente 4,5 kg, permitiendo transportarlo con facilidad. Su estructura está diseñada con materiales resistentes y su disponibilidad es limitada debido al alto costo y complejidad de su fabricación.
            </p>

            <div class="zona-compra">
                <div id="contenedor-contador" class="mb-3"></div>
                <div id="stockProducto" class="stock">Stock disponible:</div>
                <div id="mensajeStock" class="mensaje-stock"></div>
                
                <div class="botones">
                    <a href="productos.php" class="btn btn-secondary">Volver atrás</a>
                    <button type="button" id="btnAgregar" class="btn btn-cafe" onclick="agregarAlCarro()">Agregar al carro</button>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="offcanvas offcanvas-end" tabindex="-1" id="carritoLateral">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title">Tu Carrito</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas"></button>
  </div>
  <div class="offcanvas-body">
    <ul id="lista-carrito" class="list-group mb-3"></ul>
    <h4>Total: $<span id="total-carrito">0</span></h4>
    <button class="btn btn-cafe w-100 mt-3" style="background-color: #6d4c41; color: white; border: none; padding: 11px 22px;">Ir a Pagar</button>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

<script>
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

    function agregarAlCarro() {
        const cantidad = parseInt(document.getElementById("cantidad").value);
        const productoExistente = carrito.find(item => item.nombre === productoActual.nombre);

        if (productoExistente) {
            productoExistente.cantidad += cantidad;
        } else {
            carrito.push({ nombre: productoActual.nombre, precio: productoActual.precio, cantidad: cantidad });
        }
        localStorage.setItem('carrito', JSON.stringify(carrito));
        actualizarCarrito();
        var bsOffcanvas = new bootstrap.Offcanvas(document.getElementById('carritoLateral'));
        bsOffcanvas.show();
    }

    function modificarCantidad(index, cambio) {
        let nuevaCantidad = carrito[index].cantidad + cambio;
        if (nuevaCantidad > 0) {
            carrito[index].cantidad = nuevaCantidad;
        } else {
            carrito.splice(index, 1); 
        }
        localStorage.setItem('carrito', JSON.stringify(carrito));
        actualizarCarrito();
    }

    function eliminarDelCarro(index) {
        carrito.splice(index, 1);
        localStorage.setItem('carrito', JSON.stringify(carrito));
        actualizarCarrito();
    }

    function actualizarCarrito() {
        const lista = document.getElementById('lista-carrito');
        const contador = document.getElementById('contador-carrito');
        const total = document.getElementById('total-carrito');
        if(!lista) return;

        lista.innerHTML = '';
        let sumaTotal = 0;
        let cantTotal = 0;

        carrito.forEach((item, index) => {
            sumaTotal += item.precio * item.cantidad;
            cantTotal += item.cantidad;
            
            lista.innerHTML += `
            <li class="list-group-item d-flex justify-content-between align-items-center">
                <div>
                    <h6 class="my-0">${item.nombre}</h6>
                    <div class="btn-group btn-group-sm mt-2" role="group">
                        <button type="button" class="btn btn-outline-secondary" onclick="modificarCantidad(${index}, -1)">-</button>
                        <button type="button" class="btn btn-outline-secondary" disabled>${item.cantidad}</button>
                        <button type="button" class="btn btn-outline-secondary" onclick="modificarCantidad(${index}, 1)">+</button>
                    </div>
                </div>
                <div class="text-end">
                    <span class="text-muted d-block">$${(item.precio * item.cantidad).toLocaleString('es-CL')}</span>
                    <button class="btn btn-sm btn-danger mt-2" onclick="eliminarDelCarro(${index})"><i class="fa fa-trash"></i></button>
                </div>
            </li>`;
        });

        if(contador) contador.innerText = cantTotal;
        if(total) total.innerText = sumaTotal.toLocaleString('es-CL');
    }
</script>
</body>
</html>