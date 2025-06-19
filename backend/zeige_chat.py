import sqlite3

#Verbindung zur Datenbank im Hauptverzeichnis
conn = sqlite3.connect("chat.db")
cursor = conn.cursor()

#Einträge anzeigen
print("Einträge in der Datenbank:\n")
for row in cursor.execute("SELECT * FROM chat"):
    print(row)

conn.close()