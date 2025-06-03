document.addEventListener("DOMContentLoaded", function () {
    console.log("JS de modales cargado correctamente ✅");

    const modales = document.querySelectorAll(".modal");
    modales.forEach(modal => {
        modal.addEventListener("hidden.bs.modal", () => {
            // Aquí puedes limpiar contenido o cerrar cosas personalizadas si algún día lo necesitas
            console.log(`Modal ${modal.id} cerrado.`);
        });
    });
});