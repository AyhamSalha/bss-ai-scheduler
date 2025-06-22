function toggleChat() {
  const chatbox = document.getElementById("chatbox");
  chatbox.style.display = chatbox.style.display === "flex" ? "none" : "flex"; 
}

window.onload = () => {
  document.getElementById("chatbox").style.display = "none";

  const input = document.querySelector(".chat-footer input");
  const button = document.querySelector(".chat-footer button");

  button.addEventListener("click", async () => {
    const text = input.value.trim();
    if (text !== "") {
      appendMessage("user", text);
      input.value = "";

      try {
        //Anfrage an das Backend senden
        const response = await fetch("http://localhost:8000/chat", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
             benutzer: "Nutzer",
             nachricht: text
             })
        });

        //Antwort parsen
        if (response.ok) {
          const data = await response.json();
          const antwort = formatAntwort(data.response);
          appendMessage("ki", antwort);
        } 
        else {
          appendMessage("ki", "⚠️ Fehler beim Abrufen der Antwort vom Server.");
        }

      }
      catch (error) {
        appendMessage("ki", "⚠️ Der Server ist aktuell nicht erreichbar.");
        console.error("Backend-Fehler:", error);
      }
    }
  });
};
function appendMessage(sender, text) {
  const msgBox = document.getElementById("chat-messages");
  const msg = document.createElement("div");
  msg.classList.add("chat-message", sender);
  msg.innerHTML = text;
  msgBox.appendChild(msg);

  msgBox.scrollTop = msgBox.scrollHeight;
}

function formatAntwort(text) {
  return text.replace(/\n/g, "<br>");
}