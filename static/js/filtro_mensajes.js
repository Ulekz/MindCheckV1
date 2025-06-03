document.addEventListener("DOMContentLoaded", function () {
    const buscador = document.getElementById("buscador");
    const filas = document.querySelectorAll("tbody tr");

    buscador.addEventListener("input", function () {
        const texto = buscador.value.toLowerCase();

        filas.forEach(fila => {
            const nombre = fila.cells[0].textContent.toLowerCase();
            const correo = fila.cells[1].textContent.toLowerCase();

            if (nombre.includes(texto) || correo.includes(texto)) {
                fila.style.display = "";
            } else {
                fila.style.display = "none";
            }
        });
    });
});
