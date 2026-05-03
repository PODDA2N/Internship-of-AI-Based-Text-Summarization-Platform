async function summarizeText() {
    const text = document.getElementById("textInput").value;
    const file = document.getElementById("fileInput").files[0];
    const loading = document.getElementById("loading");
    const output = document.getElementById("summaryText");

    loading.style.display = "block";
    output.innerText = "";

    try {
        let response;

        // Case 1: Text input
        if (text) {
            response = await fetch("http://localhost:8000/summarize", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ text: text })
            });
        }

        // Case 2: PDF upload
        else if (file) {
            const formData = new FormData();
            formData.append("file", file);

            response = await fetch("http://localhost:8000/summarize-file", {
                method: "POST",
                body: formData
            });
        } 
        
        else {
            alert("Please enter text or upload a PDF");
            loading.style.display = "none";
            return;
        }

        const data = await response.json();
        output.innerText = data.summary;

    } catch (error) {
        output.innerText = "Error occurred!";
    }

    loading.style.display = "none";
}