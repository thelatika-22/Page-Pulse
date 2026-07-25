const analyzeBtn = document.getElementById("analyzeBtn");

analyzeBtn.addEventListener("click", async () => {

    const url = document.getElementById("urlInput").value;

    if (!url) {
        alert("Please enter a website URL.");
        return;
    }

    document.getElementById("loading").classList.remove("hidden");
    document.getElementById("results").classList.add("hidden");

    try {

        const API = "https://page-pulse-lmls.onrender.com";
       

        const response = await fetch(
            `${API}/analyze?url=${encodeURIComponent(url)}`
        );

        

        if (!response.ok) {
            const err = await response.json();
            throw new Error(err.error);
        }

        const data = await response.json();

        

        document.getElementById("title").textContent =
            data.title || "Not Found";

        document.getElementById("meta").textContent =
            data.meta_description || "Not Found";

        document.getElementById("h1").textContent =
            data.h1_count;

        document.getElementById("words").textContent =
            data.word_count;

        document.getElementById("alt").textContent =
            data.missing_alt_images;

        document.getElementById("time").textContent =
            data.response_time.toFixed(2) +"sec";

        document.getElementById("status").textContent =
            data.status_code;

        document.getElementById("results").classList.remove("hidden");

    }
    catch(error){

        alert(error.message);
        

        console.log(error);

    }

    document.getElementById("loading").classList.add("hidden");

});