// Funktion zum Umschalten der Sichtbarkeit des Chatfensters
function toggleChat() {
  const chatbox = document.getElementById("chatbox");
  chatbox.style.display = chatbox.style.display === "flex" ? "none" : "flex"; 
}

window.onload = () => {
  document.getElementById("chatbox").style.display = "none";
  const input = document.querySelector(".chat-footer input");
  const button = document.querySelector(".chat-footer button");

  // Event-Listener für den Chat-Button
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

        // Wenn die Antwort erfolgreich war, die Antwort formatieren und anzeigen
        if (response.ok) {
          const data = await response.json();
          const antwort = formatAntwort(data.response);
          appendMessage("ki", antwort);
        }
        // Wenn die Antwort nicht erfolgreich war, eine Fehlermeldung anzeigen
        else {
          appendMessage("ki", "⚠️ Fehler beim Abrufen der Antwort vom Server.");
        }
      }
      // Fehlerbehandlung
      catch (error) {
        appendMessage("ki", "⚠️ Der Server ist aktuell nicht erreichbar.");
        console.error("Backend-Fehler:", error);
      }
    }
  });

   // Beim Drücken der Enter-Taste die Nachricht senden
  input.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      button.click();
    }
  });
};

// Funktion zum Anhängen einer Nachricht an den Chat
function appendMessage(sender, text) {
  const msgBox = document.getElementById("chat-messages");
  const msg = document.createElement("div");
  msg.classList.add("chat-message", sender);

   // Aktuelle Uhrzeit im Format "HH:MM" (24-Stunden-Format)
  const time = new Date().toLocaleTimeString("de-DE", { hour: "2-digit", minute: "2-digit" });

  msg.innerHTML = `<div>${text}</div><div class="timestamp">${time}</div>`;
  msgBox.appendChild(msg);
  msgBox.scrollTop = msgBox.scrollHeight;
}

// Hilfsfunktion zum Formatieren der Antwort
function formatAntwort(text) {
  return text.replace(/\n/g, "<br>");
}

// ------------------------------------------------------------------------------
// Kalender-Interaktion
document.querySelectorAll(".calendar td").forEach(cell => {
  const tag = cell.dataset.tag;
  if (!tag) return;

  cell.addEventListener("click", () => {
  const mitarbeiter = document.getElementById("mitarbeiter").value;
  const status = document.getElementById("status").value;

  if (!mitarbeiter || !status || !cell.dataset.tag) return;

  // vorhandene Eintragung löschen
  const vorhanden = cell.querySelector(".zugewiesen");
  if (vorhanden) vorhanden.remove();

  // Klassen zurücksetzen
  cell.classList.remove("assigned", "absent");

  // neue Eintragung
  const eintrag = document.createElement("div");
  eintrag.classList.add("zugewiesen");
  eintrag.textContent = mitarbeiter;
  cell.appendChild(eintrag);
  cell.classList.add(status); // z. B. assigned oder absent
  });
});

// Funktion zum Zurücksetzen des Kalenders
function resetPlan() {
  document.querySelectorAll(".calendar td").forEach(cell => {
    const tag = cell.dataset.tag;
    if (tag) {
      cell.innerHTML = `<div class="datum">${tag}</div>`;
    } else {
      cell.innerHTML = "";
    }
    cell.classList.remove("assigned", "absent");
  });
}
// Ende of script.js