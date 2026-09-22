(() => {
  const CART_KEY = 'quesoSaborCart';
  const FAVORITES_KEY = 'quesoSaborFavorites';

  const safeParse = (value, fallback) => {
    try { return JSON.parse(value) ?? fallback; }
    catch { return fallback; }
  };

  // Se usa localStorage normalmente. Si el navegador lo bloquea al abrir archivos file://,
  // window.name mantiene una copia temporal mientras se navega en la misma pestaña.
  const storage = {
    get(key) {
      try { return localStorage.getItem(key); }
      catch {
        const fallback = safeParse(window.name, {});
        return fallback[key] ?? null;
      }
    },
    set(key, value) {
      try { localStorage.setItem(key, value); }
      catch {
        const fallback = safeParse(window.name, {});
        fallback[key] = value;
        window.name = JSON.stringify(fallback);
      }
    }
  };

  const loadCart = () => safeParse(storage.get(CART_KEY), []);
  const saveCart = cart => storage.set(CART_KEY, JSON.stringify(cart));
  const loadFavorites = () => safeParse(storage.get(FAVORITES_KEY), []);
  const saveFavorites = favorites => storage.set(FAVORITES_KEY, JSON.stringify(favorites));
  const findProduct = id => (window.QS_PRODUCTS || []).find(product => product.id === Number(id));
  const money = value => `$${value.toLocaleString('es-CL')}`;

  function showToast(message) {
    let toast = document.querySelector('.toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.className = 'toast';
      toast.setAttribute('role', 'status');
      toast.setAttribute('aria-live', 'polite');
      document.body.appendChild(toast);
    }
    toast.textContent = message;
    toast.classList.add('is-visible');
    clearTimeout(showToast.timer);
    showToast.timer = setTimeout(() => toast.classList.remove('is-visible'), 2200);
  }

  function itemCount(cart = loadCart()) {
    return cart.reduce((sum, item) => sum + item.cantidad, 0);
  }

  function updateHeaderCounters() {
    const count = itemCount();
    document.querySelectorAll('[data-cart-count]').forEach(el => { el.textContent = count; });
    const favCount = loadFavorites().length;
    document.querySelectorAll('[data-favorite-count]').forEach(el => { el.textContent = favCount; });
  }

  function injectCart() {
    if (document.querySelector('#cart-drawer')) return;
    document.body.insertAdjacentHTML('beforeend', `
      <div class="cart-overlay" data-cart-overlay></div>
      <aside class="cart-drawer" id="cart-drawer" aria-hidden="true" aria-labelledby="cart-title">
        <div class="cart-header">
          <div>
            <h2 id="cart-title">Tu carrito</h2>
            <p data-cart-summary>Tienes 0 productos</p>
          </div>
          <button class="icon-btn" type="button" data-cart-close aria-label="Cerrar carrito">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>
          </button>
        </div>
        <div class="cart-items" data-cart-items></div>
        <div class="cart-footer">
          <div class="cart-subtotal"><span>Subtotal</span><strong data-cart-subtotal>$0</strong></div>
          <div class="cart-footer__actions">
            <button class="btn btn--secondary" type="button" data-cart-empty>Vaciar carrito</button>
            <button class="btn btn--primary" type="button" data-cart-checkout>Continuar compra</button>
          </div>
        </div>
      </aside>`);
  }

  function renderCart() {
    const itemsContainer = document.querySelector('[data-cart-items]');
    if (!itemsContainer) return;
    const cart = loadCart();
    const detailed = cart
      .map(item => ({ ...item, product: findProduct(item.id) }))
      .filter(item => item.product);

    document.querySelector('[data-cart-summary]').textContent = `Tienes ${itemCount(cart)} ${itemCount(cart) === 1 ? 'producto' : 'productos'}`;
    const subtotal = detailed.reduce((sum, item) => sum + item.product.precio * item.cantidad, 0);
    document.querySelector('[data-cart-subtotal]').textContent = money(subtotal);

    if (!detailed.length) {
      itemsContainer.innerHTML = `<div class="cart-empty"><div><div class="cart-empty__icon">🧀</div><h3>Tu carrito está vacío</h3><p>Agrega alguno de nuestros quesos artesanales para verlo aquí.</p></div></div>`;
    } else {
      itemsContainer.innerHTML = detailed.map(({ product, cantidad }) => `
        <article class="cart-item">
          <img src="${product.imagen}" alt="${product.nombre}">
          <div>
            <h3>${product.nombre}</h3>
            <p class="cart-item__price">${money(product.precio)}</p>
            <div class="qty-control" aria-label="Cantidad de ${product.nombre}">
              <button class="qty-btn" type="button" data-cart-decrease="${product.id}" aria-label="Disminuir cantidad">−</button>
              <span class="qty-value">${cantidad}</span>
              <button class="qty-btn" type="button" data-cart-increase="${product.id}" aria-label="Aumentar cantidad">+</button>
            </div>
          </div>
          <button class="remove-item" type="button" data-cart-remove="${product.id}" aria-label="Eliminar ${product.nombre}">✕</button>
        </article>`).join('');
    }
    updateHeaderCounters();
  }

  function addToCart(productId) {
    const product = findProduct(productId);
    if (!product) return;
    const cart = loadCart();
    const existing = cart.find(item => item.id === product.id);
    if (existing) existing.cantidad += 1;
    else cart.push({ id: product.id, cantidad: 1 });
    saveCart(cart);
    renderCart();
    showToast(`${product.nombre} agregado al carrito`);
  }

  function changeQuantity(productId, delta) {
    const cart = loadCart();
    const item = cart.find(entry => entry.id === Number(productId));
    if (!item) return;
    item.cantidad += delta;
    const next = cart.filter(entry => entry.cantidad > 0);
    saveCart(next);
    renderCart();
  }

  function removeFromCart(productId) {
    const next = loadCart().filter(item => item.id !== Number(productId));
    saveCart(next);
    renderCart();
  }

  function emptyCart() {
    saveCart([]);
    renderCart();
    showToast('Carrito vaciado');
  }

  function openCart() {
    renderCart();
    const drawer = document.querySelector('#cart-drawer');
    const overlay = document.querySelector('[data-cart-overlay]');
    drawer.classList.add('is-open');
    overlay.classList.add('is-open');
    drawer.setAttribute('aria-hidden', 'false');
    document.body.classList.add('no-scroll');
    drawer.querySelector('[data-cart-close]').focus();
  }

  function closeCart() {
    const drawer = document.querySelector('#cart-drawer');
    const overlay = document.querySelector('[data-cart-overlay]');
    drawer?.classList.remove('is-open');
    overlay?.classList.remove('is-open');
    drawer?.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('no-scroll');
  }

  function isFavorite(productId) {
    return loadFavorites().includes(Number(productId));
  }

  function toggleFavorite(productId, button) {
    const id = Number(productId);
    const favorites = loadFavorites();
    const existing = favorites.includes(id);
    const next = existing ? favorites.filter(item => item !== id) : [...favorites, id];
    saveFavorites(next);

    document.querySelectorAll(`[data-product-id="${id}"].js-favorite`).forEach(element => {
      element.classList.toggle('is-favorite', !existing);
      element.setAttribute('aria-pressed', String(!existing));
      element.setAttribute('aria-label', !existing ? 'Quitar de favoritos' : 'Agregar a favoritos');
    });

    updateHeaderCounters();
    window.dispatchEvent(new CustomEvent('qs:favorites-changed'));
    const product = findProduct(id);
    showToast(existing ? `${product?.nombre || 'Producto'} eliminado de favoritos` : `${product?.nombre || 'Producto'} guardado en favoritos`);
  }

  function attachEvents() {
    document.addEventListener('click', event => {
      const addButton = event.target.closest('.js-add-cart');
      if (addButton) addToCart(addButton.dataset.productId);

      const favoriteButton = event.target.closest('.js-favorite');
      if (favoriteButton) toggleFavorite(favoriteButton.dataset.productId, favoriteButton);

      if (event.target.closest('[data-cart-open]')) openCart();
      if (event.target.closest('[data-cart-close]') || event.target.matches('[data-cart-overlay]')) closeCart();

      const increase = event.target.closest('[data-cart-increase]');
      const decrease = event.target.closest('[data-cart-decrease]');
      const remove = event.target.closest('[data-cart-remove]');
      if (increase) changeQuantity(increase.dataset.cartIncrease, 1);
      if (decrease) changeQuantity(decrease.dataset.cartDecrease, -1);
      if (remove) removeFromCart(remove.dataset.cartRemove);

      if (event.target.closest('[data-cart-empty]')) emptyCart();
      if (event.target.closest('[data-cart-checkout]')) showToast('Compra simulada: no se enviarán datos ni pagos.');
    });

    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && document.querySelector('#cart-drawer')?.classList.contains('is-open')) closeCart();
    });

    window.addEventListener('storage', updateHeaderCounters);
  }

  window.QuesoSabor = {
    addToCart,
    openCart,
    closeCart,
    isFavorite,
    updateHeaderCounters,
    showToast
  };

  document.addEventListener('DOMContentLoaded', () => {
    injectCart();
    attachEvents();
    renderCart();
    updateHeaderCounters();
  });
})();
