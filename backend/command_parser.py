"""
Command parser for natural language scheduling commands.
Extracts employee names and dates from text input.
"""
import re
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)


def parse_scheduling_command(text: str):
    """
    Recognize simple scheduling commands from natural language, e.g.:
        ➤ "Schedule Mustafa on Monday"
        ➤ "Plane mir Mustafa am Montag ein" (German)
    
    Returns a dictionary with name and date when such a command is recognized.
    
    Args:
        text: Input text to parse
        
    Returns:
        Dictionary with 'mitarbeiter' and 'datum' keys, or None if no valid command found
    """
    # Pattern to extract name and weekday (supports both English and German)
    patterns = [
        r"(?:plane mir |schedule |plan )?(\w+) (?:am |on )(monday|tuesday|wednesday|thursday|friday|saturday|sunday|montag|dienstag|mittwoch|donnerstag|freitag|samstag|sonntag)"
    ]
    
    # Apply pattern to the input text
    match = None
    for pattern in patterns:
        match = re.search(pattern, text.lower())
        if match:
            break
    
    if not match:
        logger.debug(f"No scheduling command found in: {text}")
        return None  # No valid scheduling command found

    # Extract data from match object
    name = match.group(1).capitalize()
    weekday = match.group(2).capitalize()

    # Map weekday to index (Monday = 0, ..., Sunday = 6)
    weekday_map = {
        "Monday": 0, "Montag": 0,
        "Tuesday": 1, "Dienstag": 1,
        "Wednesday": 2, "Mittwoch": 2,
        "Thursday": 3, "Donnerstag": 3,
        "Friday": 4, "Freitag": 4,
        "Saturday": 5, "Samstag": 5,
        "Sunday": 6, "Sonntag": 6
    }
    
    weekday_index = weekday_map.get(weekday)
    if weekday_index is None:
        logger.warning(f"Unknown weekday: {weekday}")
        return None

    # Current date and weekday (as index)
    today = datetime.today()
    today_index = today.weekday()

    # Calculate difference to find next occurrence of desired weekday
    days_difference = (weekday_index - today_index) % 7
    target_date = today + timedelta(days=days_difference)

    # Return date in ISO format (YYYY-MM-DD)
    date = target_date.strftime("%Y-%m-%d")

    logger.info(f"Parsed command: {name} on {date}")
    
    # Return recognized entry as dictionary
    return {
        "mitarbeiter": name,
        "datum": date
    }


# Keep old function name for backward compatibility
parse_plan_befehl = parse_scheduling_command
