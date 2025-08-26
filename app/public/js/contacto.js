console.log("Archivo contacto.js cargado");

function CamposVacios() {
    const nombre = document.getElementById("nombre").value.trim();
    const correo = document.getElementById("email").value.trim();
    const mensaje = document.getElementById("mensaje").value.trim();

    if (nombre === "" || correo === "" || mensaje === "") {
        Swal.fire({
            icon: 'warning',
            title: 'Campos incompletos',
            text: 'Por favor, completa todos los campos.',
        });
        return false;
    }
    return true;
}

function FormatoCorreo() {
    const correo = document.getElementById("email").value.trim();
    const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,63}$/;

    if (!regex.test(correo)) {
        Swal.fire({
            icon: 'error',
            title: 'Correo inválido',
            text: 'Por favor, ingresa un correo electrónico válido.',
        });
        return false;
    }
    return true;
}

function mensajeMinimo() {
    const mensaje = document.getElementById("mensaje").value.trim();

    if (mensaje.length < 10) {
        Swal.fire({
            icon: 'warning',
            title: 'Mensaje muy corto',
            text: 'Por favor, escribe un mensaje más detallado.',
        });
        return false;
    }
    return true;
}

function mensajeEnviado() {
    Swal.fire({
        icon: 'success',
        title: 'Mensaje enviado',
        text: 'Tu mensaje ha sido enviado correctamente.',
    });

} 

function ValidarFormulario() {
    if (!CamposVacios()) {
        return false;
    }
    if (!FormatoCorreo()) {
        return false;
    }
    if (!mensajeMinimo()) {
        return false;
    }
    if (!mensajeEnviado()) {
        return false;
    }
    return true;
} 
