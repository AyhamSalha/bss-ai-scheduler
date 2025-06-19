import sqlite3

#Verbindung zur Datenbank
conn = sqlite3.connect("chat.db")
cursor = conn.cursor()

#Lösche Einträge mit leerem benutzer oder leerer nachricht (auch nur Leerzeichen)
cursor.execute("""
    DELETE FROM chat
    WHERE TRIM(benutzer) = '' OR TRIM(nachricht) = ''
""")

#Anzahl gelöschter Zeilen
anzahl = cursor.rowcount
conn.commit()
conn.close()

print(f"{anzahl} fehlerhafte Einträge wurden gelöscht.")
