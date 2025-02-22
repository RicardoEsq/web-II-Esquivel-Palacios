document.addEventListener("DOMContentLoaded", function () {
    const orderCards = document.querySelectorAll(".order-card");

    orderCards.forEach(card => {
        card.addEventListener("click", function () {
            alert("Orden seleccionada: " + this.querySelector("p strong").innerText);
        });
    });
});
