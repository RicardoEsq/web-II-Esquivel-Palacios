document.addEventListener("DOMContentLoaded", function () {
    const button = document.querySelector("#create-user-button");

    if (button) {
        button.addEventListener("click", function (event) {
            event.preventDefault(); // Evitar el envío tradicional del formulario

            const form = document.querySelector("#create-user-form");
            const formData = new FormData(form);
            const data = {};

            // Convertir FormData a JSON
            formData.forEach((value, key) => {
                data[key] = value;
            });

            const token = document.querySelector("#csrf_token").value; // Obtener CSRF token

            fetch(USER_CREATE_URL, {
                method: "POST",
                headers: {
                    "X-CSRFToken": token,
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json()) // Convertir respuesta a JSON
            .then(value => {
                if (value.status === "success") {
                    alert("✅ Usuario creado exitosamente");
                    window.location.href = "/user/list"; // Redirigir después de crear
                } else {
                    alert("❌ Error al crear usuario: " + value.message);
                }
            })
            .catch(error => {
                console.error("Error en la solicitud:", error);
                alert("❌ Hubo un error en la solicitud.");
            });
        });
    }
});
