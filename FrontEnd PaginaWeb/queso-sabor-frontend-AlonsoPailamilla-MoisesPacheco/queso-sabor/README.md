# Queso & Sabor — Frontend

Proyecto universitario desarrollado únicamente con HTML5, CSS3 y JavaScript Vanilla.
No incluye backend, base de datos, autenticación real, APIs obligatorias ni frameworks.

## Cómo ejecutarlo

1. Descomprime la carpeta `queso-sabor`.
2. Abre `index.html` con tu navegador.
3. Navega con el menú superior entre Inicio, Productos, Sobre nosotros, Locales y Contacto.

Para una experiencia más consistente con `localStorage` entre distintas páginas, también puedes abrir la carpeta con una extensión como Live Server de VS Code. Esto no agrega backend al proyecto: solo sirve archivos estáticos en tu computador.

## Dónde cambiar los colores

Abre `css/styles.css` y modifica las variables del bloque `:root`, por ejemplo:

- `--color-primary`
- `--color-primary-dark`
- `--color-cream`
- `--color-beige`
- `--color-brown`
- `--color-text`

## Dónde cambiar los productos

Abre `js/productos.js`. Al inicio encontrarás el arreglo `products` con objetos que tienen:

- `id`
- `nombre`
- `tipo`
- `leche`
- `precio`
- `imagen`
- `destacado`
- `descripcion`

Puedes editar, quitar o agregar objetos manteniendo esa estructura.

## Dónde cambiar las imágenes

Las imágenes están en `assets/img/`. Ahora el proyecto ya incluye fotografías reales de quesos para el hero, secciones informativas y tarjetas de productos.

Si quieres reemplazarlas por otras fotografías, mantén los mismos nombres de archivo, por ejemplo:

- `hero-quesos.jpg`
- `queso-gouda.jpg`
- `queso-cabra.jpg`
- `queso-brie.jpg`
- `queso-azul.jpg`

Si cambias el nombre de una imagen de producto, recuerda actualizar también la ruta en `js/productos.js`.

## Funcionalidades implementadas

- Navegación responsive con menú hamburguesa.
- Catálogo dinámico generado con JavaScript.
- Filtros por tipo de queso, tipo de leche y precio.
- Ordenamiento y paginación.
- Carrito lateral con overlay, cantidades, eliminación y subtotal.
- Cierre del carrito con X, clic fuera o tecla Escape.
- Carrito persistente mediante `localStorage`.
- Favoritos persistentes mediante `localStorage`.
- Formulario de contacto con validación frontend.
- Formulario de comentarios con validación frontend.
- Login simulado con validación frontend.
- Diseño responsive para escritorio, tablet y móvil.
