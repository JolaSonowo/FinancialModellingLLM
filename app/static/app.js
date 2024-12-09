document.getElementById("query-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const query = document.getElementById("query").value;
    const resultElement = document.getElementById("expanded-query");

    try {
        const response = await fetch("/expand", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ query }),
        });

        if (!response.ok) {
            throw new Error("Failed to fetch the expanded query.");
        }

        const data = await response.json();
        resultElement.textContent = data.expanded_query;
    } catch (error) {
        resultElement.textContent = `Error: ${error.message}`;
    }
});
