"""Unit tests for LLM command parser."""
import pytest
from datetime import datetime, timedelta
from backend.command_parser import parse_scheduling_command


def test_parse_simple_command():
    """Test parsing simple planning command."""
    result = parse_scheduling_command("Plane mir Mustafa am Montag ein")
    assert result is not None
    assert result["mitarbeiter"] == "Mustafa"
    assert "datum" in result


def test_parse_english_command():
    """Test parsing English command."""
    result = parse_scheduling_command("Schedule Ayham on Monday")
    assert result is not None
    assert result["mitarbeiter"] == "Ayham"
    assert "datum" in result


def test_parse_different_days():
    """Test parsing with different weekdays."""
    days = ["montag", "dienstag", "mittwoch", "donnerstag", "freitag", "samstag", "sonntag"]
    names = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    
    for day, name in zip(days, names):
        result = parse_scheduling_command(f"Plane mir Ayham am {day} ein")
        assert result is not None
        assert result["mitarbeiter"] == "Ayham"


def test_parse_case_insensitive():
    """Test case insensitivity."""
    result1 = parse_scheduling_command("PLANE MIR KOUTAIBE AM MONTAG EIN")
    result2 = parse_scheduling_command("plane mir koutaibe am montag ein")
    
    assert result1 is not None
    assert result2 is not None
    assert result1["mitarbeiter"] == result2["mitarbeiter"]


def test_parse_invalid_command():
    """Test with invalid command."""
    result = parse_scheduling_command("Hello world")
    assert result is None


def test_parse_partial_match():
    """Test with partial match."""
    result = parse_scheduling_command("Plane mir")
    assert result is None


def test_parse_different_names():
    """Test with various names."""
    names = ["Ayham", "Gürhan", "Koutaibe", "Mustafa"]
    
    for name in names:
        result = parse_scheduling_command(f"Plane mir {name} am Montag ein")
        assert result is not None
        assert result["mitarbeiter"] == name
