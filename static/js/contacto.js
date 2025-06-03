document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const nombre = document.getElementById("nombre");
    const correo = document.getElementById("correo");
    const mensaje = document.getElementById("mensaje");

    form.addEventListener("submit", function (e) {
        let errores = [];

        if (!nombre.value.trim()) {
            errores.push("El nombre es obligatorio.");
        }

        const emailRegex = /^[^@]+@[^@]+\.[a-zA-Z]{2,}$/;
        if (!emailRegex.test(correo.value.trim())) {
            errores.push("El correo electrónico no es válido.");
        }

        if (!mensaje.value.trim() || mensaje.value.length < 10) {
            errores.push("El mensaje debe tener al menos 10 caracteres.");
        }

        if (errores.length > 0) {
            e.preventDefault();
            alert(errores.join("\\n"));
        }
    });
});
