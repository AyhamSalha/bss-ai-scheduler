"""Unit tests for chat endpoints."""
import pytest
from fastapi.testclient import TestClient
from backend.main import app
import os

client = TestClient(app)


def test_read_root():
    """Test root endpoint returns health status."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert "status" in data


def test_health_check():
    """Test detailed health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "database" in data
    assert "version" in data


def test_chat_endpoint():
    """Test chat endpoint with valid input."""
    response = client.post(
        "/chat",
        json={"benutzer": "TestUser", "nachricht": "Hallo"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "response" in data


def test_chat_endpoint_invalid_input():
    """Test chat endpoint with missing fields."""
    response = client.post(
        "/chat",
        json={"benutzer": "TestUser"}
    )
    assert response.status_code == 422


def test_get_history():
    """Test history endpoint."""
    response = client.get("/history")
    assert response.status_code == 200
    data = response.json()
    assert "history" in data
    assert isinstance(data["history"], list)


def test_get_history_with_limit():
    """Test history endpoint with custom limit."""
    response = client.get("/history?limit=10")
    assert response.status_code == 200
    data = response.json()
    assert "history" in data
    assert len(data["history"]) <= 10
