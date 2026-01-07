
const ocean = document.querySelector(".ocean");

async function processText() {
  const task = document.getElementById("task");
  const textBox = document.getElementById("inputText");
  const output = document.getElementById("output");
  const button = document.querySelector("button");

  const text = textBox.value.trim();
  if (!text) {
    output.innerText = "⚠️ Please enter some text";
    return;
  }

  button.innerText = "Processing...";
  button.disabled = true;
  output.innerText = "⏳ Processing your text...";

  try {
    // 🔴 SPAM
    if (task.value === "spam") {
      const response = await fetch("http://127.0.0.1:5000/predict-spam", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();
      console.log("Spam API response:", data);

      output.innerText = "✅ Prediction: " + data.prediction;
    }

    // 🟢 GRAMMAR
    else if (task.value === "grammar") {
      const response = await fetch("http://127.0.0.1:5000/grammar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();
      console.log("Grammar API response:", data);

      output.innerText =
        "✅ Corrected Sentence:\n" + data.corrected_text;
    }

  } catch (error) {
    console.error(error);
    output.innerText = "❌ Error connecting to server";
  }

  button.innerText = "Process";
  button.disabled = false;
}


// Create bubble
function createBubble() {
    const bubble = document.createElement("div");
    bubble.className = "bubble";

    const size = Math.random() * 15 + 20;
    bubble.style.width = size + "px";
    bubble.style.height = size + "px";

    bubble.style.left = Math.random() * 100 + "vw";

    const duration = Math.random() * 8 + 8;
    bubble.style.animationDuration = duration + "s";

    // Hover → bubble speeds up (clumsy air feel)
    bubble.addEventListener("mouseenter", () => {
        bubble.style.animationDuration = "1s";
        bubble.style.opacity = "0";
    });

    ocean.appendChild(bubble);

    setTimeout(() => {
        bubble.remove();
    }, duration * 1000);
}

// Create bubbles slowly (natural)
setInterval(createBubble, 600);
