document.querySelector("form").addEventListener("submit", async function(event) {

    event.preventDefault();

    let formData = new FormData(this);

    await fetch("/", {
        method: "POST",
        body: formData
    });

});
document.getElementById("Input_marcas").focus();