from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
import sqlite3
import logging
from contextlib import asynccontextmanager
import os

from backend.schemas import ChatEintrag
from backend.llm_utils import generiere_antwort
from backend.config import get_settings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events."""
    logger.info("Starting BSS KI-Agent application...")
    init_db()
    yield
    logger.info("Shutting down BSS KI-Agent application...")


app = FastAPI(
    title="BSS KI-Agent API",
    description="AI-powered staff scheduling system with natural language processing",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
origins = settings.cors_origins.split(",") if "," in settings.cors_origins else [settings.cors_origins]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (frontend)
frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")
    logger.info(f"Frontend mounted at /static from {frontend_path}")

# Error handlers
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle validation errors."""
    logger.error(f"Validation error: {exc.errors()}")
    return JSONResponse(
        status_code=422,
        content={
            "error": "Ungültige Eingabe",
            "details": exc.errors()
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Handle general exceptions."""
    logger.exception(f"Unexpected error: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"error": "Ein interner Serverfehler ist aufgetreten"}
    )

# Request/Response models
class ChatRequest(BaseModel):
    """Chat request from frontend."""
    benutzer: str
    nachricht: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "benutzer": "Nutzer",
                "nachricht": "Plane mir Ayham am Dienstag ein"
            }
        }

# Database initialization
def init_db():
    """Initialize SQLite database."""
    try:
        conn = sqlite3.connect(settings.database_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                benutzer TEXT NOT NULL,
                nachricht TEXT NOT NULL,
                timestamp TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")
        raise

@app.get("/", tags=["Health"])
def read_root():
    """Health check endpoint - also serves frontend."""
    from fastapi.responses import FileResponse
    frontend_index = os.path.join(frontend_path, "index.html")
    if os.path.exists(frontend_index):
        return FileResponse(frontend_index)
    return {
        "message": "KI-Agent läuft",
        "version": "1.0.0",
        "status": "healthy"
    }


@app.get("/health", tags=["Health"])
def health_check():
    """Detailed health check."""
    try:
        # Check database connection
        conn = sqlite3.connect(settings.database_path)
        conn.close()
        db_status = "healthy"
    except Exception as e:
        logger.error(f"Database health check failed: {e}")
        db_status = "unhealthy"
    
    return {
        "status": "healthy" if db_status == "healthy" else "unhealthy",
        "database": db_status,
        "version": "1.0.0"
    }

@app.post("/chat", tags=["Chat"])
async def chat(request: ChatRequest):
    """Process chat message and return AI response."""
    try:
        logger.info(f"Received chat from {request.benutzer}: {request.nachricht}")
        
        # Save message to database
        conn = sqlite3.connect(settings.database_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO chat (benutzer, nachricht) VALUES (?, ?)",
            (request.benutzer, request.nachricht)
        )
        conn.commit()
        conn.close()
        
        # Generate LLM response
        antwort = generiere_antwort(request.nachricht)
        logger.info(f"Generated response: {antwort.get('response', '')}")
        
        return antwort
    except Exception as e:
        logger.error(f"Chat processing failed: {e}")
        raise HTTPException(status_code=500, detail="Fehler bei der Verarbeitung der Nachricht")

@app.post("/eintrag", tags=["Chat"])
def neuer_chat_eintrag(eintrag: ChatEintrag):
    """Create a new chat entry (for testing)."""
    try:
        conn = sqlite3.connect(settings.database_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO chat (benutzer, nachricht, timestamp) VALUES (?, ?, ?)",
            (eintrag.benutzer, eintrag.nachricht, eintrag.timestamp)
        )
        conn.commit()
        conn.close()
        logger.info(f"Created chat entry for {eintrag.benutzer}")
        return {"status": "Eintrag gespeichert"}
    except Exception as e:
        logger.error(f"Failed to create chat entry: {e}")
        raise HTTPException(status_code=500, detail="Fehler beim Speichern")


@app.get("/history", tags=["Chat"])
def get_history(limit: int = 50):
    """Get chat history."""
    try:
        conn = sqlite3.connect(settings.database_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, benutzer, nachricht, timestamp FROM chat ORDER BY id DESC LIMIT ?",
            (limit,)
        )
        rows = cursor.fetchall()
        conn.close()
        
        history = [
            {
                "id": row[0],
                "benutzer": row[1],
                "nachricht": row[2],
                "timestamp": row[3]
            }
            for row in rows
        ]
        return {"history": history}
    except Exception as e:
        logger.error(f"Failed to fetch history: {e}")
        raise HTTPException(status_code=500, detail="Fehler beim Abrufen des Verlaufs")
