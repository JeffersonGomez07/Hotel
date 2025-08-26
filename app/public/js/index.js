document.addEventListener("DOMContentLoaded", () => {
  console.log("🌐 Aplicación de Reservaciones Cargada");

  mostrarFechaActual();
  manejarMenuResponsive();
  mostrarMensajeTemporal();
  mostrarMensajesSweetAlert();  // 💡 Función para los mensajes con SweetAlert
});

/**
 * Muestra la fecha actual en un elemento con ID "fecha-hoy".
 */
function mostrarFechaActual() {
  const fechaElemento = document.getElementById("fecha-hoy");
  if (fechaElemento) {
    const hoy = new Date();
    const fechaFormateada = hoy.toLocaleDateString("es-CR", {
      weekday: "long",
      year: "numeric",
      month: "long",
      day: "numeric",
    });
    fechaElemento.textContent = fechaFormateada;
  }
}

/**
 * Muestra u oculta el menú para dispositivos móviles.
 */
function manejarMenuResponsive() {
  const btnMenu = document.getElementById("btn-menu");
  const nav = document.getElementById("nav-principal");

  if (btnMenu && nav) {
    btnMenu.addEventListener("click", () => {
      nav.classList.toggle("activo");
    });
  }
}

/**
 * Elimina mensajes de alerta simples (por si usas divs de alerta).
 */
function mostrarMensajeTemporal() {
  const alerta = document.querySelector(".alerta-flash");
  if (alerta) {
    setTimeout(() => {
      alerta.style.opacity = 0;
      alerta.remove();
    }, 4000); // 4 segundos
  }
}

/**
 * Muestra los mensajes flash de Flask como SweetAlert.
 */
function mostrarMensajesSweetAlert() {
  const flashContainer = document.getElementById("flash-messages");
  if (!flashContainer) return;

  const rawMessages = flashContainer.dataset.messages;
  if (!rawMessages) return;

  try {
    const messages = JSON.parse(rawMessages);

    if (Array.isArray(messages)) {
      messages.forEach(([category, message]) => {
        let icon = "info";
        if (category === "success") icon = "success";
        else if (category === "warning") icon = "warning";
        else if (category === "danger" || category === "error") icon = "error";

        Swal.fire({
          icon: icon,
          title: message,
          timer: 3000,
          timerProgressBar: true,
          showConfirmButton: false,
        });
      });
    }
  } catch (e) {
    console.error("Error al procesar mensajes flash:", e);
  }
}
