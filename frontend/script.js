// Function to toggle chat window visibility
function toggleChat() {
  const chatbox = document.getElementById("chatbox");
  chatbox.style.display = chatbox.style.display === "flex" ? "none" : "flex"; 
}

window.onload = () => {
  document.getElementById("chatbox").style.display = "none";
  const input = document.querySelector(".chat-footer input");
  const button = document.querySelector(".chat-footer button");

  // Event listener for chat button
  button.addEventListener("click", async () => {
    const text = input.value.trim();
    if (text !== "") {
      appendMessage("user", text);
      input.value = "";

      try {
        // Send request to backend
        const response = await fetch("http://localhost:8000/chat", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            benutzer: "User",
            nachricht: text
          })
        });

        if (response.ok) {
          const data = await response.json();

          // Robust response check
          if (typeof data.response === "string") {
            const answer = formatAnswer(data.response);
            appendMessage("ki", answer);  // Keep "ki" for CSS compatibility
          } else {
            console.warn("Unexpected format from data.response:", data.response);
            appendMessage("ki", "⚠️ The server response was empty or invalid.");
          }

          // Add calendar entry (optional)
          if (data.eintrag) {
            const d = data.eintrag.datum;
            if (!entries[d]) entries[d] = [];
            entries[d].push(data.eintrag);
            generateCalendar();
          }
        }
        // If response was not successful, show error message
        else {
          appendMessage("ki", "⚠️ Error retrieving response from server.");
        }
      }
      // Error handling
      catch (error) {
        appendMessage("ki", "⚠️ The server is currently unreachable.");
        console.error("Backend error:", error);
      }
    }
  });

  // Send message when Enter key is pressed
  input.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      button.click();
    }
  });
};

// Function to append a message to the chat
function appendMessage(sender, text) {
  const msgBox = document.getElementById("chat-messages");
  const msg = document.createElement("div");
  msg.classList.add("chat-message", sender);

  // Current time in "HH:MM" format (24-hour)
  const time = new Date().toLocaleTimeString("en-US", { hour: "2-digit", minute: "2-digit", hour12: false });

  msg.innerHTML = `<div>${text}</div><div class="timestamp">${time}</div>`;
  msgBox.appendChild(msg);
  msgBox.scrollTop = msgBox.scrollHeight;
}

// Helper function to format the answer
function formatAnswer(text) {
  return text.replace(/\n/g, "<br>");
}

// Keep old function name for compatibility
const formatAntwort = formatAnswer;

// -------------------------------------------------------------------------------------------------------------------------
// Calendar interaction
const entries = {};
const eintraege = entries; // Keep German name for compatibility
let selectedDate = "";

const form = document.getElementById("eintragForm");
const overlay = document.getElementById("overlay");

document.querySelector(".close-btn").addEventListener("click", closeForm);
document.getElementById("cancelBtn").addEventListener("click", closeForm);
overlay.addEventListener("click", closeForm);

window.addEventListener("keydown", e => {
  if (e.key === "Escape" && form.classList.contains("active")) {
    closeForm();
  }
});

//Generate time options for selects
function generateTimeOptions() {
  const times = [];
  for (let h = 8; h <= 18; h++) {
    for (let m = 0; m < 60; m += 15) {
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

fillTimeSelects();

function generateCalendar() {
  const tbody = document.getElementById("calendarBody");
  tbody.innerHTML = "";
  
  // Use current month/year instead of hardcoded July 2025
  const now = new Date();
  const year = now.getFullYear();
  const month = now.getMonth(); // 0-indexed (0 = January)
  
  // Update calendar title
  const monthNames = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"];
  document.getElementById("calendar-title").textContent = 
    `Staff Scheduling – ${monthNames[month]} ${year}`;
  
  const firstDay = new Date(year, month, 1);
  const lastDay = new Date(year, month + 1, 0);
  const daysInMonth = lastDay.getDate();
  const startWeekday = (firstDay.getDay() + 6) % 7; // Monday = 0
  
  let day = 1;

  for (let i = 0; i < 6; i++) {
    const row = document.createElement("tr");

    for (let j = 0; j < 7; j++) {
      const cell = document.createElement("td");

      if ((i === 0 && j < startWeekday) || day > daysInMonth) {
        cell.innerHTML = "";
      } else {
        const date = `${year}-${String(month + 1).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
        cell.innerHTML = `<strong>${day}</strong>`;
        cell.addEventListener("click", () => openForm(date));

        (entries[date] || []).forEach((e, index) => {
          const div = document.createElement("div");
          div.className = `eintrag ${e.verfuegbar === "Ja" ? "verfuegbar" : "nicht-verfuegbar"}`;
          div.innerHTML = `${e.title}<br>${e.uhrzeit} – ${e.mitarbeiter}<br>Available: ${e.verfuegbar}`;

          const editBtn = document.createElement("button");
          editBtn.innerText = "⚙️";
          editBtn.title = "Edit";
          editBtn.onclick = (ev) => {
            ev.stopPropagation();
            openForm(date, index, e);
          };

          const deleteBtn = document.createElement("button");
          deleteBtn.innerText = "✖️";
          deleteBtn.title = "Delete";
          deleteBtn.style.right = "20px";
          deleteBtn.onclick = (ev) => {
            ev.stopPropagation();
            entries[date].splice(index, 1);
            generateCalendar();
          };

          div.appendChild(editBtn);
          div.appendChild(deleteBtn);
          cell.appendChild(div);
        });

        day++;
      }

      row.appendChild(cell);
    }

    tbody.appendChild(row);
  }
}

function openForm(date, index = null, data = null) {
  selectedDate = date;
  document.getElementById("von").value = date;
  document.getElementById("bis").value = date;
  document.getElementById("title").value = data ? data.title : "";
  document.getElementById("uhrzeit").value = data ? data.uhrzeit.split("–")[0] : "";
  document.getElementById("endzeit").value = data ? data.uhrzeit.split("–")[1] : "";
  document.getElementById("mitarbeiter").value = data ? data.mitarbeiter : "Ayham";
  document.getElementById("verfuegbar").value = data ? data.verfuegbar : "Ja";
  document.getElementById("bearbeiteDatum").value = date;
  document.getElementById("bearbeiteIndex").value = index !== null ? index : "";
  overlay.classList.add("active");
  form.classList.add("active");
}

function closeForm() {
  overlay.classList.remove("active");
  form.classList.remove("active");
  form.reset();
  document.getElementById("bearbeiteIndex").value = "";
  document.getElementById("bearbeiteDatum").value = "";
}

// Keep German function names for compatibility
const öffneForm = openForm;
const schliessenForm = closeForm;
const erzeugeKalender = generateCalendar;

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const date = document.getElementById("bearbeiteDatum").value || selectedDate;
  const index = document.getElementById("bearbeiteIndex").value;
  const title = document.getElementById("title").value.trim();
  const uhrzeit = document.getElementById("uhrzeit").value;
  const endzeit = document.getElementById("endzeit").value;
  const von = document.getElementById("von").value;
  const bis = document.getElementById("bis").value;
  const mitarbeiter = document.getElementById("mitarbeiter").value;
  const verfuegbar = document.getElementById("verfuegbar").value;

  const start = new Date(von);
  const end = new Date(bis);

  for (let d = new Date(start); d <= end; d.setDate(d.getDate() + 1)) {
    const dat = d.toISOString().split("T")[0];
    if (!entries[dat]) entries[dat] = [];

    if (dat === date && index !== "") {
      entries[dat][index] = {
        title,
        uhrzeit: `${uhrzeit}–${endzeit}`,
        mitarbeiter,
        verfuegbar
      };
    } else {
      entries[dat].push({
        title,
        uhrzeit: `${uhrzeit}–${endzeit}`,
        mitarbeiter,
        verfuegbar
      });
    }
  }

  closeForm();
  generateCalendar();
});

generateCalendar();

// End of script.js

