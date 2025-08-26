const API_BASE_URL = "/api"; // Puedes cambiar esto si usás prefijo

/**
 * Verifica la disponibilidad de una habitación en una fecha.
 * @param {string} tipoHabitacion - El tipo de habitación (ej. "doble").
 * @param {string} fecha - La fecha en formato YYYY-MM-DD.
 * @returns {Promise<Object>} - Resultado con disponibilidad.
 */
export async function getDisponibilidadHabitacion(tipoHabitacion, fecha) {
  try {
    const response = await fetch(`${API_BASE_URL}/disponibilidad`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ tipo: tipoHabitacion, fecha }),
    });

    if (!response.ok) {
      throw new Error("Error en la respuesta del servidor");
    }

    return await response.json(); // { disponible: true/false, mensaje: "" }

  } catch (error) {
    console.error("Error al consultar disponibilidad:", error);
    return { disponible: false, mensaje: "Error de conexión con el servidor" };
  }
}

/**
 * Envía los datos del formulario de reservación al backend.
 * @param {Object} data - Los datos del formulario de reservación.
 * @returns {Promise<Object>} - Resultado con éxito o error.
 */
export async function enviarFormularioReservacion(data) {
  try {
    const response = await fetch(`${API_BASE_URL}/reservar`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error("No se pudo enviar la reservación.");
    }

    return await response.json(); // { exito: true, mensaje: "Reservación realizada" }

  } catch (error) {
    console.error("Error al enviar la reservación:", error);
    return { exito: false, mensaje: "Error al enviar la reservación" };
  }
}
