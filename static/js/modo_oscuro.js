document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("toggle-dark");
    const body = document.body;

    // Función para aplicar modo
    const aplicarModo = (modo) => {
        if (modo === "oscuro") {
            body.classList.add("dark-mode");
            body.classList.remove("light-mode");
            toggle.innerHTML = "☀️"; // Icono de sol
        } else {
            body.classList.remove("dark-mode");
            body.classList.add("light-mode");
            toggle.innerHTML = "🌙"; // Icono de luna
        }
    };

    // Ver preferencia guardada o usar la del sistema si es primera vez
    let modoGuardado = localStorage.getItem("modo");
    if (!modoGuardado) {
        // Preferencia del sistema
        const prefiereOscuro = window.matchMedia('(prefers-color-scheme: dark)').matches;
        modoGuardado = prefiereOscuro ? "oscuro" : "claro";
    }

    aplicarModo(modoGuardado);

    // Evento para cambiar de modo al hacer clic
    toggle.addEventListener("click", () => {
        const modoActual = body.classList.contains("dark-mode") ? "oscuro" : "claro";
        const nuevoModo = modoActual === "oscuro" ? "claro" : "oscuro";
        localStorage.setItem("modo", nuevoModo);
        aplicarModo(nuevoModo);
    });
});
