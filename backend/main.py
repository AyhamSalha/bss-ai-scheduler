from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel
#Pydantic-Modell importieren
from backend.schemas import ChatEintrag

app = FastAPI()

#Datenbank initialisieren
def init_db():
    connection = sqlite3.connect("chat.db") #Verbindung zur SQLite-Datenbank
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            benutzer TEXT NOT NULL,
            nachricht TEXT NOT NULL,
            timestamp TEXT
        )
    """)
    connection.commit() #Speichern der Änderungen
    connection.close() #Schließen der Verbindung

init_db() 

#GET-Endpunkt zur Statusanzeige
@app.get("/")
def read_root():
    return {"message": "KI-Agent läuft"} #Status testen

#POST-Endpunkt zum Speichern eines Eintrags
@app.post("/eintrag")
def neuer_chat_eintrag(eintrag: ChatEintrag):
    connection = sqlite3.connect("chat.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO chat (benutzer, nachricht, timestamp) VALUES (?, ?, ?)",
        (eintrag.benutzer, eintrag.nachricht, eintrag.timestamp) #Aus dem Request Daten einfügen
    )
    connection.commit()
    connection.close() 
    return {"status": "Eintrag gespeichert"} #Nachricht zurückgeben

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    return {"response": "Dies ist eine Platzhalterantwort vom KI-Agenten."}