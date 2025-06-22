// Funktion zum Öffnen und Schließen des Chatfensters
function toggleChat() {
  const chatbox = document.getElementById("chatbox");
  // Überprüfen, ob das Chatfenster sichtbar ist
  chatbox.style.display = chatbox.style.display === "flex" ? "none" : "flex"; 
}
// Event-Listener für den Button zum Öffnen des Chatfensters
window.onload = () => {
  // Button zum Öffnen des Chatfensters
  document.getElementById("chatbox").style.display = "none";

  const input = document.querySelector(".chat-footer input");
  const button = document.querySelector(".chat-footer button");

  // Event-Listener für den Button zum Senden der Nachricht
  button.addEventListener("click", async () => {
    const text = input.value.trim();
    // Überprüfen, ob der Text nicht leer ist
    if (text !== "") {
      appendMessage("user", text);
      input.value = "";

      // Anfrage an das Backend senden
      // und die Antwort anzeigen
      try {
        // Anfrage an das Backend senden
        const response = await fetch("http://localhost:8000/chat", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ message: text })
        });
        
        // Überprüfen, ob die Antwort erfolgreich war
        // Antwort parsen
        if (response.ok) {
          const data = await response.json();
          const antwort = formatAntwort(data.response);
          appendMessage("ki", antwort);
        } 
        // Wenn die Antwort nicht erfolgreich war, Fehlermeldung anzeigen
        else {
          appendMessage("ki", "⚠️ Fehler beim Abrufen der Antwort vom Server.");
        }

      }
      // Fehler beim Abrufen der Antwort vom Server, falls Backend nicht erreichbar
      catch (error) {
        appendMessage("ki", "⚠️ Der Server ist aktuell nicht erreichbar.");
        console.error("Backend-Fehler:", error);
      }
    }
  });
};
// Funktion zum Anhängen einer Nachricht an das Chatfenster
function appendMessage(sender, text) {
  const msgBox = document.getElementById("chat-messages");
  const msg = document.createElement("div");
  msg.classList.add("chat-message", sender);
  msg.innerHTML = text;
  msgBox.appendChild(msg);

  // Scrollen zum Ende des Chatfensters
  // damit die neueste Nachricht sichtbar ist
  msgBox.scrollTop = msgBox.scrollHeight;
}

// Funktion zum Formatieren der Antwort
function formatAntwort(text) {
  return text.replace(/\n/g, "<br>");
}

// Ende von script.js