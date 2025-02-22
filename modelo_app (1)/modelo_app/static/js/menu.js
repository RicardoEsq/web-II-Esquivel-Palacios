document.addEventListener("DOMContentLoaded", function () {
    const menuOptions = document.querySelectorAll(".menu-options div");

    menuOptions.forEach(option => {
        // Agregar efecto de hover cambiando el color del texto
        option.addEventListener("mouseover", function () {
            this.style.backgroundColor = "#007bff"; // Azul al pasar el mouse
            this.style.color = "white"; 
        });

        option.addEventListener("mouseout", function () {
            this.style.backgroundColor = "transparent"; // Regresa al estado original
            this.style.color = "black";
        });

        // Hacer clic en una opción la redirige a su enlace interno
        option.addEventListener("click", function () {
            const link = this.querySelector("a");
            if (link) {
                window.location.href = link.href; // Redirige a la URL del enlace
            }
        });
    });
});
