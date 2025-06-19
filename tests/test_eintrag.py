import sys
import os

# Projektpfad erweitern, damit backend.main importiert werden kann
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_leerer_benutzername():
    print("Test wird ausgeführt")
    response = client.post("/eintrag", json={
        "benutzer": "",
        "nachricht": "Hallo",
        "timestamp": "2025-06-19 12:00:00"
    })
    assert response.status_code == 422
    data = response.json()
    assert "error" in data
    assert data["error"] == "Ungültige Eingabe"

def test_leere_nachricht():
    response = client.post("/eintrag", json={
        "benutzer": "Kotay",
        "nachricht": "",
        "timestamp": "2025-06-19 12:00:00"
    })
    assert response.status_code == 422
    data = response.json()
    assert "error" in data
    assert data["error"] == "Ungültige Eingabe"
