(() => {
  function initMobileMenu() {
    const toggle = document.querySelector('[data-menu-toggle]');
    const menu = document.querySelector('[data-nav-links]');
    if (!toggle || !menu) return;

    const closeMenu = () => {
      menu.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
    };

    toggle.addEventListener('click', () => {
      const isOpen = menu.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(isOpen));
    });

    menu.addEventListener('click', event => {
      if (event.target.closest('a')) closeMenu();
    });

    document.addEventListener('click', event => {
      if (!menu.classList.contains('is-open')) return;
      if (!event.target.closest('[data-nav-links]') && !event.target.closest('[data-menu-toggle]')) closeMenu();
    });

    window.addEventListener('resize', () => {
      if (window.innerWidth > 980) closeMenu();
    });
  }

  function markActiveNavigation() {
    const current = document.body.dataset.page;
    if (!current) return;
    document.querySelectorAll('[data-nav-page]').forEach(link => {
      const active = link.dataset.navPage === current;
      link.classList.toggle('active', active);
      if (active) link.setAttribute('aria-current', 'page');
      else link.removeAttribute('aria-current');
    });
  }

  function updateYear() {
    document.querySelectorAll('[data-current-year]').forEach(el => { el.textContent = new Date().getFullYear(); });
  }

  document.addEventListener('DOMContentLoaded', () => {
    initMobileMenu();
    markActiveNavigation();
    updateYear();
  });
})();
