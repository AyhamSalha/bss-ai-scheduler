import re  #Modul für reguläre Ausdrücke
from datetime import datetime, timedelta  #Für Datums- und Zeitberechnungen

def parse_plan_befehl(text: str):
    """
    Erkennt einfache Planungsbefehle aus natürlicher Sprache, z. B.:
        ➤ "Plane mir Mustafa am Montag ein"
    Gibt ein Dictionary mit Name und Datum zurück, wenn ein solcher Befehl erkannt wird.
    """
    #Ausdruck zum Extrahieren von Namen und Wochentag
    pattern = r"plane mir (\w+) am (montag|dienstag|mittwoch|donnerstag|freitag|samstag|sonntag)"
    
    #Anwendung des Patterns auf den eingegebenen Text
    match = re.search(pattern, text.lower())
    if not match:
        return None  #Kein gültiger Planungsbefehl gefunden

    #Extrahierte Daten aus dem Match-Objekt
    name = match.group(1).capitalize()        #z. B. "mustafa" → "Mustafa"
    wochentag = match.group(2).capitalize()   #z. B. "montag" → "Montag"

    #Liste zur Umwandlung des Wochentags in einen Index (Montag = 0, ..., Sonntag = 6)
    wochentag_index = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"].index(wochentag)

    #Aktuelles Datum und aktueller Wochentag (als Index)
    heute = datetime.today()
    heute_index = heute.weekday()

    #Differenz berechnen, um das nächste Vorkommen des gewünschten Wochentags zu finden
    tage_differenz = (wochentag_index - heute_index) % 7
    ziel_datum = heute + timedelta(days=tage_differenz)

    #Datum im ISO-Format (YYYY-MM-DD) zurückgeben
    datum = ziel_datum.strftime("%Y-%m-%d")

    #Rückgabe des erkannten Eintrags als Dictionary
    return {
        "mitarbeiter": name,
        "datum": datum
    }
