"""
Show Chat Database Utility
Displays all entries from the chat database.
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

# Display entries
print("Database entries:\n")
for row in cursor.execute("SELECT * FROM chat"):
    print(row)

conn.close()
