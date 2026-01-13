"""
Clean Chat Database Utility
Removes entries with empty username or message fields from the database.
"""
import sqlite3
import sys
import os

# Add parent directory to path to import config
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from backend.config import get_settings

settings = get_settings()

# Connect to the database
conn = sqlite3.connect(settings.database_path)
cursor = conn.cursor()

# Delete entries with empty username or message (including whitespace-only)
cursor.execute("""
    DELETE FROM chat
    WHERE TRIM(benutzer) = '' OR TRIM(nachricht) = ''
""")

# Get number of deleted rows
count = cursor.rowcount
conn.commit()
conn.close()

print(f"{count} invalid entries were deleted.")

