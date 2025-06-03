document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("toggle-dark");
    const icono = document.getElementById("icono-modo");
    const html = document.documentElement;

    const aplicarModo = (modo) => {
        if (modo === "oscuro") {
            html.setAttribute("data-theme", "oscuro");
            icono.classList.remove("fa-moon");
            icono.classList.add("fa-sun");
        } else {
            html.setAttribute("data-theme", "claro");
            icono.classList.remove("fa-sun");
            icono.classList.add("fa-moon");
        }
    };

    let modoGuardado = localStorage.getItem("modo");
    if (!modoGuardado) {
        const prefiereOscuro = window.matchMedia('(prefers-color-scheme: dark)').matches;
        modoGuardado = prefiereOscuro ? "oscuro" : "claro";
    }

    aplicarModo(modoGuardado);

    toggle.addEventListener("click", () => {
        const modoActual = html.getAttribute("data-theme");
        const nuevoModo = modoActual === "oscuro" ? "claro" : "oscuro";
        localStorage.setItem("modo", nuevoModo);
        aplicarModo(nuevoModo);
    });
});
