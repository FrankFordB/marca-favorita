document.addEventListener("DOMContentLoaded", () => {
    const miForm = document.getElementById("miForm");
    const input = document.getElementById("Input_marcas");

    if (input) input.focus();

    if (miForm) {
        miForm.addEventListener("submit", async function (e) {
            e.preventDefault();

            const formData = new FormData(this);
            const res = await fetch("/", {
                method: "POST",
                body: formData
            });

            const html = await res.text();
            document.open();
            document.write(html);
            document.close();
        });
    }
});