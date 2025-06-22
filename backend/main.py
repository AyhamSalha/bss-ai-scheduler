from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import sqlite3

from backend.schemas import ChatEintrag
from backend.llm_utils import generiere_antwort  #LLM-Antwortfunktion importiert

app = FastAPI()

#CORS für Frontend-Anfragen aktivieren
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Fehlerausgabe im JSON-Format bei ungültiger Eingabe
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": "Ungültige Eingabe",
            "details": exc.errors()
        }
    )

#Modell für die Chat-Anfrage vom Frontend
class ChatRequest(BaseModel):
    benutzer: str
    nachricht: str

#Datenbank initialisieren
def init_db():
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            benutzer TEXT NOT NULL,
            nachricht TEXT NOT NULL,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

#Test-Endpunkt
@app.get("/")
def read_root():
    return {"message": "KI-Agent läuft"}

#Haupt-POST-Endpunkt: speichert Nachricht + antwortet mit LLM
@app.post("/chat")
async def chat(request: ChatRequest):
    #Nachricht in Datenbank speichern
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chat (benutzer, nachricht, timestamp) VALUES (?, ?, datetime('now'))",
        (request.benutzer, request.nachricht)
    )
    conn.commit()
    conn.close()

    #LLM-Antwort generieren
    antwort = generiere_antwort(request.nachricht)

    return {"response": antwort}

#Swagger-Test-Endpunkt
@app.post("/eintrag")
def neuer_chat_eintrag(eintrag: ChatEintrag):
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chat (benutzer, nachricht, timestamp) VALUES (?, ?, ?)",
        (eintrag.benutzer, eintrag.nachricht, eintrag.timestamp)
    )
    conn.commit()
    conn.close()
    return {"status": "Eintrag gespeichert"}
