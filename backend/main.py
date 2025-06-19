from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import sqlite3
from pydantic import BaseModel, Field
#Pydantic-Modell importieren
from backend.schemas import ChatEintrag

app = FastAPI()

# Fehlerausgabe im JSON-Format bei ungültiger Eingabe (HTTP 422)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": "Ungültige Eingabe",
            "details": exc.errors()
        }
    )

# Separates Modell für /chat-Endpunkt
class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="Chat-Nachricht darf nicht leer sein")

# Datenbank initialisieren (falls noch nicht vorhanden)
def init_db():
    connection = sqlite3.connect("chat.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            benutzer TEXT NOT NULL,
            nachricht TEXT NOT NULL,
            timestamp TEXT
        )
    """)
    connection.commit()
    connection.close()

init_db()

# Status-Endpunkt
@app.get("/")
def read_root():
    return {"message": "KI-Agent läuft"}

# Chat-Eintrag speichern
@app.post("/eintrag")
def neuer_chat_eintrag(eintrag: ChatEintrag):
    connection = sqlite3.connect("chat.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO chat (benutzer, nachricht, timestamp) VALUES (?, ?, ?)",
        (eintrag.benutzer, eintrag.nachricht, eintrag.timestamp)
    )
    connection.commit()
    connection.close()
    return {"status": "Eintrag gespeichert"}

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    return {"response": "Dies ist eine Platzhalterantwort vom KI-Agenten."}