from pydantic import BaseModel, Field
from typing import Optional

# Modell für einen Chat-Eintrag – wird im Endpunkt /eintrag verwendet
class ChatEintrag(BaseModel):
    id: Optional[int] = None  # optional, wird von der Datenbank gesetzt

    benutzer: str = Field(..., min_length=1, description="Benutzer darf nicht leer sein")
    nachricht: str = Field(..., min_length=1, description="Nachricht darf nicht leer sein")

    timestamp: Optional[str] = None  # darf leer bleiben
