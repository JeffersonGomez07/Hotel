console.log('archivo cargado');

document.addEventListener('DOMContentLoaded', function () {
  const flashContainer = document.getElementById('flash-messages');
  if (!flashContainer) return;

  let rawMessages = flashContainer.dataset.messages;

  try {
    const messages = JSON.parse(rawMessages);

    if (Array.isArray(messages)) {
      messages.forEach(([category, message]) => {
        let icon = 'info';
        if (category === 'success') icon = 'success';
        else if (category === 'warning') icon = 'warning';
        else if (category === 'danger' || category === 'error') icon = 'error';

        Swal.fire({
          icon: icon,
          title: message,
          timer: 3000,
          timerProgressBar: true,
          showConfirmButton: false
        });
      });
    }
  } catch (e) {
    console.error('Error al procesar mensajes flash:', e);
  }
});

function CamposVacios() {
  const email = document.getElementById('email').value.trim();
  const password = document.getElementById('password').value.trim();

  if (!email || !password) {
      Swal.fire({
          icon: 'warning',
          title: 'Campos incompletos',
          text: 'Por favor, completa todos los campos.'
      });
      return false;
  }
  return true;
}

function FormatoCorreo() {
  const email = document.getElementById('email').value.trim();
  const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,63}$/;

  if (!regex.test(email)) {
      Swal.fire({
          icon: 'error',
          title: 'Correo inválido',
          text: 'Por favor, ingresa un correo electrónico válido.'
      });
      return false;
  }
  return true;
}

function ValidarFormulario() {
  return CamposVacios() && FormatoCorreo();
}
