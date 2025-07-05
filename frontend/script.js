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

// -------------------------------------------------------------------------------------------------------------------------
// Kalender-Interaktion
const eintraege = {};
let selectedDate = "";

const form = document.getElementById("eintragForm");
const overlay = document.getElementById("overlay");

document.querySelector(".close-btn").addEventListener("click", schliessenForm);
document.getElementById("cancelBtn").addEventListener("click", schliessenForm);

window.addEventListener("keydown", e => {
  if (e.key === "Escape" && form.classList.contains("active")) {
    schliessenForm();
  }
});

// Generate time options for selects
function generateTimeOptions() {
  const times = [];
  for (let h = 8; h <= 18; h++) {
    for (let m = 0; m < 60; m += 15) {
      // Skip times after 18:00 exactly (only allow up to 18:00)
      if (h === 18 && m > 0) break;

      const hh = String(h).padStart(2, '0');
      const mm = String(m).padStart(2, '0');
      times.push(`${hh}:${mm}`);
    }
  }
  return times;
}

function fillTimeSelects() {
  const times = generateTimeOptions();
  const uhrzeitSelect = document.getElementById("uhrzeit");
  const endzeitSelect = document.getElementById("endzeit");

  uhrzeitSelect.innerHTML = times.map(t => `<option value="${t}">${t}</option>`).join('');
  endzeitSelect.innerHTML = times.map(t => `<option value="${t}">${t}</option>`).join('');
}

// Call once on page load
fillTimeSelects();

function erzeugeKalender() {
  const tbody = document.getElementById("calendarBody");
  tbody.innerHTML = "";
  let tag = 1;
  const startWochentag = 1; // Dienstag=1 for July 1, 2025
  const tageImMonat = 31;

  for (let i = 0; i < 5; i++) {
    const row = document.createElement("tr");

    for (let j = 0; j < 7; j++) {
      const cell = document.createElement("td");

      if (i === 0 && j < startWochentag) {
        cell.innerHTML = "";
      } else if (tag <= tageImMonat) {
        const datum = `2025-07-${String(tag).padStart(2, "0")}`;
        cell.innerHTML = `<strong>${tag}</strong>`;
        cell.addEventListener("click", () => öffneForm(datum));

        (eintraege[datum] || []).forEach((e, index) => {
          const div = document.createElement("div");
          div.className = `eintrag ${e.verfuegbar === "Ja" ? "verfuegbar" : "nicht-verfuegbar"}`;
          div.innerHTML = `${e.title}<br>${e.uhrzeit} – ${e.mitarbeiter}<br>Verfügbar: ${e.verfuegbar}`;

          const editBtn = document.createElement("button");
          editBtn.innerText = "⚙️";
          editBtn.title = "Bearbeiten";
          editBtn.onclick = (ev) => {
            ev.stopPropagation();
            öffneForm(datum, index, e);
          };

          const deleteBtn = document.createElement("button");
          deleteBtn.innerText = "✖️";
          deleteBtn.title = "Löschen";
          deleteBtn.style.right = "20px";
          deleteBtn.onclick = (ev) => {
            ev.stopPropagation();
            eintraege[datum].splice(index, 1);
            erzeugeKalender();
          };

          div.appendChild(editBtn);
          div.appendChild(deleteBtn);
          cell.appendChild(div);
        });

        tag++;
      }

      row.appendChild(cell);
    }

    tbody.appendChild(row);
  }
}

function öffneForm(datum, index = null, data = null) {
  selectedDate = datum;
  document.getElementById("von").value = datum;
  document.getElementById("bis").value = datum;
  document.getElementById("title").value = data ? data.title : "";
  document.getElementById("uhrzeit").value = data ? data.uhrzeit.split("–")[0] : "";
  document.getElementById("endzeit").value = data ? data.uhrzeit.split("–")[1] : "";
  document.getElementById("mitarbeiter").value = data ? data.mitarbeiter : "Ayham";
  document.getElementById("verfuegbar").value = data ? data.verfuegbar : "Ja";
  document.getElementById("bearbeiteDatum").value = datum;
  document.getElementById("bearbeiteIndex").value = index !== null ? index : "";
  overlay.classList.add("active");
  form.classList.add("active");
}

function schliessenForm() {
  overlay.classList.remove("active");
  form.classList.remove("active");
  form.reset();
  document.getElementById("bearbeiteIndex").value = "";
  document.getElementById("bearbeiteDatum").value = "";
}

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const datum = document.getElementById("bearbeiteDatum").value || selectedDate;
  const index = document.getElementById("bearbeiteIndex").value;
  const title = document.getElementById("title").value.trim();
  const uhrzeit = document.getElementById("uhrzeit").value;
  const endzeit = document.getElementById("endzeit").value;
  const von = document.getElementById("von").value;
  const bis = document.getElementById("bis").value;
  const mitarbeiter = document.getElementById("mitarbeiter").value;
  const verfuegbar = document.getElementById("verfuegbar").value;

  const start = new Date(von);
  const ende = new Date(bis);

  for (let d = new Date(start); d <= ende; d.setDate(d.getDate() + 1)) {
    const dat = d.toISOString().split("T")[0];
    if (!eintraege[dat]) eintraege[dat] = [];

    if (dat === datum && index !== "") {
      eintraege[dat][index] = {
        title,
        uhrzeit: `${uhrzeit}–${endzeit}`,
        mitarbeiter,
        verfuegbar
      };
    } else {
      eintraege[dat].push({
        title,
        uhrzeit: `${uhrzeit}–${endzeit}`,
        mitarbeiter,
        verfuegbar
      });
    }
  }

  schliessenForm();
  erzeugeKalender();
});

erzeugeKalender();

// Ende of script.js