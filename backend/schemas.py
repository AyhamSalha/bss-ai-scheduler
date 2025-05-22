from pydantic import BaseModel
from typing import Optional

#Definiert die Struktur der Chatdaten
class ChatEintrag(BaseModel):
    id: Optional[int]
    benutzer: str
    nachricht: str
    timestamp: Optional[str]

 #Hinweis: Dieses Modell ist keine echte Datenbankstruktur, sondern dient nur zur Datenprüfung & Kommunikation über die API