(() => {
  const products = [
    { id: 1, nombre: 'Queso Gouda Artesanal', tipo: 'Maduro', leche: 'Vaca', precio: 8990, imagen: 'assets/img/queso-gouda.jpg', destacado: true, descripcion: 'Suave, mantecoso y de maduración equilibrada.' },
    { id: 2, nombre: 'Queso de Cabra', tipo: 'Fresco', leche: 'Cabra', precio: 7490, imagen: 'assets/img/queso-cabra.jpg', destacado: true, descripcion: 'Fresco, cremoso y con un toque levemente ácido.' },
    { id: 3, nombre: 'Queso Chanco', tipo: 'Semimaduro', leche: 'Vaca', precio: 6990, imagen: 'assets/img/queso-chanco.jpg', destacado: true, descripcion: 'Clásico chileno de textura firme y sabor delicado.' },
    { id: 4, nombre: 'Queso Brie', tipo: 'Cremoso', leche: 'Vaca', precio: 9490, imagen: 'assets/img/queso-brie.jpg', destacado: true, descripcion: 'Interior cremoso y corteza suave de sabor elegante.' },
    { id: 5, nombre: 'Queso Camembert', tipo: 'Cremoso', leche: 'Vaca', precio: 9990, imagen: 'assets/img/queso-camembert.jpg', destacado: false, descripcion: 'Aromático, untuoso y perfecto para tablas.' },
    { id: 6, nombre: 'Queso Azul', tipo: 'Azul', leche: 'Vaca', precio: 10990, imagen: 'assets/img/queso-azul.jpg', destacado: true, descripcion: 'Intenso y persistente, con vetas azules naturales.' },
    { id: 7, nombre: 'Queso Mantecoso', tipo: 'Semimaduro', leche: 'Vaca', precio: 6590, imagen: 'assets/img/queso-mantecoso.jpg', destacado: false, descripcion: 'Mantecoso, flexible y muy versátil para cocinar.' },
    { id: 8, nombre: 'Queso Ahumado', tipo: 'Maduro', leche: 'Vaca', precio: 9290, imagen: 'assets/img/queso-ahumado.jpg', destacado: true, descripcion: 'Notas ahumadas suaves y final cálido.' },
    { id: 9, nombre: 'Parmesano Artesanal', tipo: 'Maduro', leche: 'Vaca', precio: 11990, imagen: 'assets/img/queso-parmesano.jpg', destacado: false, descripcion: 'Granulado, intenso y de larga maduración.' },
    { id: 10, nombre: 'Queso de Oveja', tipo: 'Maduro', leche: 'Oveja', precio: 12490, imagen: 'assets/img/queso-oveja.jpg', destacado: false, descripcion: 'Sabor profundo y textura compacta.' },
    { id: 11, nombre: 'Queso Cremoso Mixto', tipo: 'Cremoso', leche: 'Mixta', precio: 8290, imagen: 'assets/img/queso-cremoso.jpg', destacado: false, descripcion: 'Mezcla de leches con textura suave y untuosa.' },
    { id: 12, nombre: 'Queso Provolone', tipo: 'Semimaduro', leche: 'Vaca', precio: 8790, imagen: 'assets/img/queso-provolone.jpg', destacado: false, descripcion: 'Ideal para fundir, con sabor redondo y aromático.' },
    { id: 13, nombre: 'Queso Gruyère', tipo: 'Maduro', leche: 'Vaca', precio: 12990, imagen: 'assets/img/queso-gruyere.jpg', destacado: false, descripcion: 'Firme, complejo y con suaves notas a frutos secos.' },
    { id: 14, nombre: 'Queso Fresco Campesino', tipo: 'Fresco', leche: 'Vaca', precio: 5490, imagen: 'assets/img/queso-fresco.jpg', destacado: false, descripcion: 'Ligero, húmedo y pensado para consumo diario.' },
    { id: 15, nombre: 'Queso de Cabra con Pimienta', tipo: 'Semimaduro', leche: 'Cabra', precio: 9790, imagen: 'assets/img/queso-pimienta.jpg', destacado: false, descripcion: 'Cabra semimadura con un final especiado y elegante.' }
  ];

  window.QS_PRODUCTS = products;

  const money = value => `$${value.toLocaleString('es-CL')}`;

  function productCard(product) {
    const favorite = window.QuesoSabor?.isFavorite(product.id) || false;
    return `
      <article class="product-card">
        <div class="product-card__image-wrap">
          <img class="product-card__image" src="${product.imagen}" alt="${product.nombre}" loading="lazy">
          <button class="favorite-btn js-favorite ${favorite ? 'is-favorite' : ''}" type="button" data-product-id="${product.id}" aria-label="${favorite ? 'Quitar de favoritos' : 'Agregar a favoritos'}" aria-pressed="${favorite}">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 0 0-7.8 7.8l1.1 1.1L12 21l7.8-7.5 1.1-1.1a5.5 5.5 0 0 0-.1-7.8Z"/></svg>
          </button>
        </div>
        <div class="product-card__body">
          <div class="product-meta"><span>${product.tipo}</span><span>•</span><span>Leche de ${product.leche.toLowerCase()}</span></div>
          <h3>${product.nombre}</h3>
          <p class="product-card__desc">${product.descripcion}</p>
          <div class="product-card__footer">
            <span class="product-price">${money(product.precio)}</span>
            <button class="btn btn--primary js-add-cart" type="button" data-product-id="${product.id}">Agregar</button>
          </div>
        </div>
      </article>`;
  }

  function renderFeatured() {
    const container = document.querySelector('[data-featured-products]');
    if (!container) return;
    container.innerHTML = products.filter(product => product.destacado).slice(0, 6).map(productCard).join('');
  }

  function initCatalog() {
    const grid = document.querySelector('[data-product-grid]');
    if (!grid) return;

    const count = document.querySelector('[data-catalog-count]');
    const pagination = document.querySelector('[data-pagination]');
    const sortSelect = document.querySelector('#sort-products');
    const filterPanel = document.querySelector('#filters-panel');
    const mobileToggle = document.querySelector('[data-filter-toggle]');
    const clearFilters = document.querySelector('[data-clear-filters]');
    const minRange = document.querySelector('#price-min');
    const maxRange = document.querySelector('#price-max');
    const minValue = document.querySelector('[data-min-price]');
    const maxValue = document.querySelector('[data-max-price]');
    const typeInputs = [...document.querySelectorAll('input[name="tipo"]')];
    const milkInputs = [...document.querySelectorAll('input[name="leche"]')];

    // Si venimos desde una categoría del inicio, aplicamos ese filtro automáticamente.
    const params = new URLSearchParams(window.location.search);
    const initialTypes = params.getAll('tipo');
    const initialMilks = params.getAll('leche');

    typeInputs.forEach(input => {
      input.checked = initialTypes.includes(input.value);
    });

    milkInputs.forEach(input => {
      input.checked = initialMilks.includes(input.value);
    });

    const state = {
      page: 1,
      perPage: 6,
      favoriteOnly: window.location.hash === '#favoritos'
    };

    function selectedValues(inputs) {
      return inputs.filter(input => input.checked).map(input => input.value);
    }

    function filteredProducts() {
      const selectedTypes = selectedValues(typeInputs);
      const selectedMilks = selectedValues(milkInputs);
      let min = Number(minRange.value);
      let max = Number(maxRange.value);
      if (min > max) [min, max] = [max, min];

      let list = products.filter(product => {
        const typeOk = selectedTypes.length === 0 || selectedTypes.includes(product.tipo);
        const milkOk = selectedMilks.length === 0 || selectedMilks.includes(product.leche);
        const priceOk = product.precio >= min && product.precio <= max;
        const favOk = !state.favoriteOnly || window.QuesoSabor?.isFavorite(product.id);
        return typeOk && milkOk && priceOk && favOk;
      });

      switch (sortSelect.value) {
        case 'price-asc': list.sort((a, b) => a.precio - b.precio); break;
        case 'price-desc': list.sort((a, b) => b.precio - a.precio); break;
        case 'name-asc': list.sort((a, b) => a.nombre.localeCompare(b.nombre, 'es')); break;
        case 'name-desc': list.sort((a, b) => b.nombre.localeCompare(a.nombre, 'es')); break;
        default: list.sort((a, b) => Number(b.destacado) - Number(a.destacado) || a.id - b.id);
      }
      return list;
    }

    function renderPagination(total) {
      const totalPages = Math.max(1, Math.ceil(total / state.perPage));
      if (state.page > totalPages) state.page = totalPages;

      const pages = Array.from({ length: totalPages }, (_, index) => index + 1)
        .map(page => `<button class="page-btn ${page === state.page ? 'active' : ''}" type="button" data-page="${page}" aria-label="Ir a la página ${page}" ${page === state.page ? 'aria-current="page"' : ''}>${page}</button>`)
        .join('');

      pagination.innerHTML = `
        <button class="page-btn" type="button" data-page="prev" aria-label="Página anterior" ${state.page === 1 ? 'disabled' : ''}>←</button>
        ${pages}
        <button class="page-btn" type="button" data-page="next" aria-label="Página siguiente" ${state.page === totalPages ? 'disabled' : ''}>→</button>`;
    }

    function render() {
      const list = filteredProducts();
      const totalPages = Math.max(1, Math.ceil(list.length / state.perPage));
      if (state.page > totalPages) state.page = totalPages;
      const start = (state.page - 1) * state.perPage;
      const visible = list.slice(start, start + state.perPage);

      count.textContent = state.favoriteOnly
        ? `Mostrando ${visible.length} de ${list.length} favoritos`
        : `Mostrando ${visible.length} de ${list.length} productos`;

      grid.innerHTML = visible.length
        ? visible.map(productCard).join('')
        : `<div class="empty-state"><h3>No encontramos productos</h3><p>Prueba ajustando los filtros o quitando alguna selección.</p></div>`;

      renderPagination(list.length);
    }

    function updatePriceLabels() {
      let min = Number(minRange.value);
      let max = Number(maxRange.value);
      if (min > max) {
        if (document.activeElement === minRange) maxRange.value = min;
        else minRange.value = max;
      }
      minValue.textContent = money(Number(minRange.value));
      maxValue.textContent = money(Number(maxRange.value));
    }

    function filtersChanged() {
      state.page = 1;
      updatePriceLabels();
      render();
    }

    [...typeInputs, ...milkInputs, minRange, maxRange].forEach(control => control.addEventListener('input', filtersChanged));
    sortSelect.addEventListener('change', filtersChanged);

    pagination.addEventListener('click', event => {
      const button = event.target.closest('[data-page]');
      if (!button || button.disabled) return;
      const list = filteredProducts();
      const totalPages = Math.max(1, Math.ceil(list.length / state.perPage));
      if (button.dataset.page === 'prev') state.page = Math.max(1, state.page - 1);
      else if (button.dataset.page === 'next') state.page = Math.min(totalPages, state.page + 1);
      else state.page = Number(button.dataset.page);
      render();
      grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });

    mobileToggle?.addEventListener('click', () => {
      const isOpen = filterPanel.classList.toggle('is-open');
      mobileToggle.setAttribute('aria-expanded', String(isOpen));
      mobileToggle.textContent = isOpen ? 'Ocultar filtros' : 'Mostrar filtros';
    });

    clearFilters?.addEventListener('click', () => {
      [...typeInputs, ...milkInputs].forEach(input => { input.checked = false; });
      minRange.value = minRange.min;
      maxRange.value = maxRange.max;
      sortSelect.value = 'popular';
      state.favoriteOnly = false;
      if (window.location.hash === '#favoritos') history.replaceState(null, '', 'productos.html');
      filtersChanged();
    });

    window.addEventListener('hashchange', () => {
      state.favoriteOnly = window.location.hash === '#favoritos';
      state.page = 1;
      render();
    });

    window.addEventListener('qs:favorites-changed', render);

    updatePriceLabels();
    render();
  }

  document.addEventListener('DOMContentLoaded', () => {
    renderFeatured();
    initCatalog();
  });
})();
