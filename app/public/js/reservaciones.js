console.log("Archivo reservaciones.js cargado");

function ValidarCampos() {
  const nombre = document.getElementById("nombre").value.trim();
  const email = document.getElementById("email").value.trim();
  const checkin = document.getElementById("checkin").value;
  const checkout = document.getElementById("checkout").value;
  const habitacion = document.getElementById("habitacion").value;
  const adultos = parseInt(document.getElementById("adultos").value);
  const ninos = parseInt(document.getElementById("ninos").value);

  const hoy = new Date().toISOString().split("T")[0];

  if (!nombre || !email || !checkin || !checkout || !habitacion) {
    Swal.fire("Campos incompletos", "Por favor, completa todos los campos obligatorios.", "error");
    return null;
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    Swal.fire("Correo inválido", "Ingresa un correo electrónico válido.", "error");
    return null;
  }

  if (checkin < hoy) {
    Swal.fire("Fecha inválida", "La fecha de llegada no puede ser anterior a hoy.", "error");
    return null;
  }

  if (checkout <= checkin) {
    Swal.fire("Fecha inválida", "La fecha de salida debe ser posterior a la de llegada.", "error");
    return null;
  }

  if (isNaN(adultos) || adultos < 1) {
    Swal.fire("Cantidad inválida", "Debe haber al menos un adulto por reservación.", "error");
    return null;
  }

  if (isNaN(ninos) || ninos < 0) {
    Swal.fire("Cantidad inválida", "El número de niños no puede ser negativo.", "error");
    return null;
  }

  return {
    nombre,
    email,
    checkin,
    checkout,
    habitacion,
    adultos,
    ninos
  };
}

document.getElementById("reservacionForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const datos = ValidarCampos();
  if (!datos) return;

  console.log("Datos a enviar:", datos);

  fetch("/reservaciones", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(datos)
  })
    .then(async response => {
      const contentType = response.headers.get("content-type") || "";

      if (!response.ok) {
        if (contentType.includes("application/json")) {
          const errorData = await response.json();
          throw new Error(errorData.error || "Error en la solicitud");
        } else {
          const text = await response.text();
          throw new Error(text || "Error en la solicitud");
        }
      }

      if (contentType.includes("application/json")) {
        return response.json();
      } else {
        const text = await response.text();
        throw new Error("Respuesta inesperada del servidor: " + text);
      }
    })
    .then(data => {
      Swal.fire({
        icon: "success",
        title: "Reservación exitosa",
        text: data.mensaje || "Tu reservación ha sido registrada correctamente.",
      });
      document.getElementById("reservacionForm").reset();
    })
    .catch(error => {
      Swal.fire({
        icon: "error",
        title: "Error",
        text: error.message,
      });
      console.error("Error:", error);
    });
});
document.addEventListener("DOMContentLoaded", () => {
  const flashContainer = document.getElementById("flash-messages");
  if (!flashContainer) return;

  const rawMessages = flashContainer.dataset.messages;

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
});
