"""Data models for the application."""
from pydantic import BaseModel, Field
from typing import Optional


class ChatEntry(BaseModel):
    """Model for a chat entry - used in the /eintrag endpoint."""
    id: Optional[int] = None  # Optional, set by database
    benutzer: str = Field(..., min_length=1, description="Username cannot be empty")
    nachricht: str = Field(..., min_length=1, description="Message cannot be empty")
    timestamp: Optional[str] = None  # Can be empty


# Keep old name for backward compatibility
ChatEintrag = ChatEntry
