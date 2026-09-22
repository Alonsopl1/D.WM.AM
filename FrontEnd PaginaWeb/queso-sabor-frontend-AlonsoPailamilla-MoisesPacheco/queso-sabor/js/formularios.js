(() => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  function showFieldError(input, message) {
    const error = input.closest('.form-group')?.querySelector('.field-error');
    if (error) error.textContent = message;
    input.setAttribute('aria-invalid', message ? 'true' : 'false');
  }

  function clearFormErrors(form) {
    form.querySelectorAll('.field-error').forEach(el => { el.textContent = ''; });
    form.querySelectorAll('[aria-invalid]').forEach(el => el.setAttribute('aria-invalid', 'false'));
  }

  function setStatus(form, message) {
    const status = form.querySelector('.form-status');
    if (!status) return;
    status.textContent = message;
    status.hidden = false;
  }

  function initLogin() {
    const form = document.querySelector('#login-form');
    if (!form) return;

    form.addEventListener('submit', event => {
      event.preventDefault();
      clearFormErrors(form);
      form.querySelector('.form-status').hidden = true;
      const user = form.elements.usuario;
      const password = form.elements.password;
      let valid = true;

      if (!user.value.trim()) {
        showFieldError(user, 'Ingresa tu correo o nombre de usuario.');
        valid = false;
      } else if (user.value.includes('@') && !emailRegex.test(user.value.trim())) {
        showFieldError(user, 'El formato del correo no es válido.');
        valid = false;
      }

      if (!password.value) {
        showFieldError(password, 'Ingresa tu contraseña.');
        valid = false;
      } else if (password.value.length < 6) {
        showFieldError(password, 'La contraseña debe tener al menos 6 caracteres.');
        valid = false;
      }

      if (valid) setStatus(form, 'Inicio de sesión simulado correctamente.');
    });

    document.querySelector('[data-create-account]')?.addEventListener('click', event => {
      event.preventDefault();
      setStatus(form, 'Registro simulado: esta versión del proyecto no crea cuentas reales.');
    });
  }

  function initContact() {
    const form = document.querySelector('#contact-form');
    if (!form) return;

    form.addEventListener('submit', event => {
      event.preventDefault();
      clearFormErrors(form);
      form.querySelector('.form-status').hidden = true;
      let valid = true;
      const name = form.elements.nombre;
      const email = form.elements.correo;
      const subject = form.elements.asunto;
      const message = form.elements.mensaje;

      if (name.value.trim().length < 2) { showFieldError(name, 'Escribe tu nombre.'); valid = false; }
      if (!emailRegex.test(email.value.trim())) { showFieldError(email, 'Escribe un correo válido.'); valid = false; }
      if (!subject.value.trim()) { showFieldError(subject, 'Indica el asunto.'); valid = false; }
      if (message.value.trim().length < 10) { showFieldError(message, 'El mensaje debe tener al menos 10 caracteres.'); valid = false; }

      if (valid) {
        setStatus(form, '¡Gracias por contactarnos! Hemos recibido tu mensaje.');
        form.reset();
      }
    });
  }

  function initFeedback() {
    const form = document.querySelector('#feedback-form');
    if (!form) return;

    form.addEventListener('submit', event => {
      event.preventDefault();
      clearFormErrors(form);
      form.querySelector('.form-status').hidden = true;
      let valid = true;
      const email = form.elements.correo;
      const message = form.elements.comentario;

      if (!emailRegex.test(email.value.trim())) { showFieldError(email, 'Escribe un correo válido.'); valid = false; }
      if (message.value.trim().length < 8) { showFieldError(message, 'Cuéntanos un poco más para poder mejorar.'); valid = false; }

      if (valid) {
        setStatus(form, '¡Gracias por ayudarnos a mejorar!');
        form.reset();
      }
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    initLogin();
    initContact();
    initFeedback();
  });
})();
