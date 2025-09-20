console.log("Script loaded");

document.getElementById("articleForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("email").value;
  const url = document.getElementById("url").value;

  const payload = { email, article_url: url };

  document.getElementById("status").innerText = "Sending request...";

  try {
    const response = await fetch("http://127.0.0.1:8000/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await response.json();
    document.getElementById("status").innerText = data.message || "Submitted successfully!";
  } catch (err) {
    console.error(err);
    document.getElementById("status").innerText = "Error sending request.";
  }
});