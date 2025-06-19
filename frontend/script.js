function toggleChat() {
  const chatbox = document.getElementById("chatbox");
  chatbox.style.display = chatbox.style.display === "flex" ? "none" : "flex";
}

window.onload = () => {
  document.getElementById("chatbox").style.display = "none";

  const input = document.querySelector(".chat-footer input");
  const button = document.querySelector(".chat-footer button");

  button.addEventListener("click", () => {
    const text = input.value.trim();
    if (text !== "") {
      appendMessage("user", text);
      input.value = "";

      // KI-Antwort (Platzhalter)
      setTimeout(() => {
        appendMessage("ki", "Danke für deine Nachricht! (Platzhalter)");
      }, 500);
    }
  });
};

function appendMessage(sender, text) {
  const msgBox = document.getElementById("chat-messages");
  const msg = document.createElement("div");
  msg.classList.add("chat-message", sender);
  msg.textContent = text;
  msgBox.appendChild(msg);

  // Auto-scroll ans Ende
  msgBox.scrollTop = msgBox.scrollHeight;
}
