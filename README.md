# KI-Agent für Personaleinsatzplanung (BSS)

## Projektvision

Ziel war die Entwicklung eines intelligenten Assistenzsystems zur Unterstützung der Personaleinsatzplanung. Der KI-Agent agiert über eine benutzerfreundliche Chatoberfläche und ermöglicht die Verwaltung von Verfügbarkeiten sowie das Eintragen von Einsätzen direkt im Kalender. Das System unterstützt Planungsverantwortliche dabei, Einsätze effizient zu koordinieren – lokal, datenschutzkonform und benutzerfreundlich.

---

## Inhaltsverzeichnis

1. [Beschreibung](#beschreibung)
2. [Funktionen](#funktionen)
3. [Nicht-funktionale-Anforderungen](#nicht-funktionale-anforderungen)
4. [Aktueller Stand](#aktueller-Stand)
5. [Systemanforderungen](#systemanforderungen)
6. [Externe-Schnittstellen](#externe-schnittstellen)
7. [Qualitätsanforderungen](#qualitätsanforderungen)
8. [Technologiestack](#technologiestack)
9. [Installation](#installation)
10. [Verwendung](#verwendung)
11. [API-Endpunkte & Beispielanfragen](#api-endpunkte--beispielanfragen) 
12. [Verwertungsplan](#verwertungsplan)
13. [Lizenz](#lizenz)
14. [Kontakt](#kontakt)

---

## Beschreibung

Dieses System ermöglicht die intuitive Personaleinsatzplanung über eine Chat-Oberfläche, die mit einem lokal betriebenen KI-Agenten verbunden ist. Über natürliche Spracheingaben können Nutzer:innen Verfügbarkeiten verwalten und Einsatzwünsche direkt übermitteln. Die KI interpretiert diese Eingaben mithilfe von Regex und generiert daraus Kalendereinträge.

Das Backend basiert auf FastAPI und stellt über eine REST-API verschiedene Funktionen bereit, wie das Eintragen, Abrufen und Verwalten von Planungsinformationen. Die Datenhaltung erfolgt lokal in einer SQLite-Datenbank – vollständig ohne Cloud-Anbindung, um Datenschutz zu gewährleisten.

***Hauptmerkmale:***
- *Chatbasierte Einsatzplanung mit lokalem KI-Agenten (TinyLlama)*
- *Verfügbarkeits- und Einsatzverwaltung über eine grafische Kalenderoberfläche*
- *Speicherung und Abruf des Chatverlaufs*
- *Lokaler, datenschutzkonformer Betrieb*
- *Modularer Aufbau mit klarer Trennung von Frontend, Backend, Datenbank und KI*

**Hintergrund zur Entwicklung :**  
Ursprünglich war geplant, einen externen Kundenkalender über eine API anzubinden. Da jedoch keine realen Daten bereitgestellt wurden, wurde eine eigene Kalenderlösung implementiert. Diese Lösung ermöglicht es, Verfügbarkeiten direkt per Klick im Kalender zu setzen und per Texteingabe neue Einsätze zu planen.

- Beispielhafte Eingabe:

„Plane mir Gürhan am Dienstag ein“

- Ergebnis:

Die KI erkennt den Namen, das Datum und erstellt automatisch den passenden Kalendereintrag, sofern der Server aktiv ist.

---

## Funktionen

1. **Chatbasierte Einsatzplanung**  
Einfache Planung direkt über eine Chat-Oberfläche.


2. **KI-Interpretation**  
Planung per natürlicher Sprache durch Regex + LLM.

3. **Interaktiver Kalender**  
Darstellung & Bearbeitung von Einträgen.

4. **Verfügbarkeitsverwaltung**  
Manuelle Auswahl verfügbarer Tage für Mitarbeitende.

5. **Chatverlauf**   
Speicherung von Anfragen & Antworten.

6. **Fehlermeldungen**  
Anzeige bei Serverfehlern oder Kommunikationsproblemen.

7. **Lokaler Betrieb**  
Alle Daten bleiben auf dem lokalen System.

---

## Nicht-funktionale Anforderungen
**Datenschutz:** Keine Cloud-Anbindung – alle Daten verbleiben lokal

**Modularität:** Saubere Trennung von Frontend, Backend, Datenbank und KI-Anbindung

**Kompatibilität:** Austauschbare KI-Modelle (z. B. TinyLlama) über REST-API integrierbar

**Erweiterbarkeit:** Zukunftsfähig für Zusatzfunktionen

**Plattformunabhängigkeit:** Lokaler Betrieb unter Windows, macOS und Linux möglich

**Installierbarkeit:** Keine spezielle Infrastruktur nötig – läuft mit Standard-Tools lokal

---

## Aktueller Stand

Der KI-Agent reagiert nur auf konkrete Planungsanfragen und schlägt keine Mitarbeitenden proaktiv vor.

Eingaben wie „Plane mir Ayham am Dienstag ein“ führen zur Erstellung eines Eintrags im Kalender (wenn Server aktiv).

Wenn der Server nicht läuft, wird im Chat eine entsprechende Warnung angezeigt („Der Server ist aktuell nicht erreichbar“).

Verfügbarkeiten können zusätzlich direkt im Kalender gesetzt werden.

Der Kalender zeigt visuell, wer wann verfügbar ist und welche Einträge über die KI geplant wurden.

---

## Systemanforderungen

*Betriebssystem:*

- Windows, macOS, Linux

*Software:*

- Python 3.10 oder höher
- SQLite (lokal)
- Git
- Lokales LLM (TinyLlama)

*Abhängigkeiten:*
- uvicorn, fastapi, torch, transformers, accelerate

---

## Externe Schnittstellen
- **Webbrowser (Benutzerschnittstelle)**

- **REST-API (FastAPI)** JSON-basierte Schnittstelle

- **POST /chat** – Nutzeranfrage senden

- **GET /history** – Chatverlauf abrufen

- **Datenbank:** Speicherung von Anfragen, Antworten, Nutzerdaten

- **LLM-Modell (z. B. TinyLlama):** Zugriff über lokale API
---

## Qualitätsanforderungen

• **Zuverlässigkeit**:  
Stabiler Chatbot mit Fehlerbehandlung bei leeren oder fehlerhaften Antworten.  
• **Antwortgeschwindigkeit**:  
 < 1 Sekunde Reaktionszeit bei Einzelanfragen unter realistischen Bedingungen.  
• **Benutzerfreundlichkeit**:  
Intuitive Oberfläche mit strukturiertem Kalender, direkter Eingabe und Chatverlauf.  
• **Wartbarkeit**:   
Modularer, gut kommentierter Code mit Git-Versionskontrolle für einfache Erweiterung.

---

## Technologiestack

• **Frontend**: HTML, CSS, JavaScript + Fetch API  
• **Backend/API**: FastAPI in Python  
• **LLM-Anbindung**: Lokal installiertes LLM (TinyLlama)  
• **Datenbank**: SQLite (lokal)  
• **Kommunikation**: REST-API  
• **Server**: Uvicorn (lokal)    
• **Editor**: Visual Studio Code  

---

## Installation

1. Stellen Sie sicher, dass Python (mindestens Version 3.10), Git und das lokale LLM (z. B. TinyLlama)
installiert und betriebsbereit sind.

2. Klonen Sie das Repository auf Ihren lokalen Rechner:
```
git clone https://gitlab.rz.htw-berlin.de/softwareentwicklungsprojekt/sose2025/team-14-personaleinsatzplanung-bss.git
```
3. Installieren Sie die notwendigen Python-Abhängigkeiten mit:

   ```pip install -r requirements.txt```

4. Starten Sie den lokalen Server:

   ```uvicorn main:app --reload```

---

## Verwendung
1. Öffnen Sie einen Webbrowser und rufen Sie http://localhost:8000 auf. 
2. Einsatzanfrage über den Chat senden:  
Beispiel: Plane mir Koutaibe am Dienstag ein.
3. System antwortet mit:   Koutaibe wurde am 2025-07-15 eingeplant.
4. Eintrag erscheint im Kalender.
5. Verfügbarkeit kann direkt über Kalender gesetzt werden
6. Bei Serverfehlern erscheinen entsprechende Warnungen

---

## API-Endpunkte & Beispielanfragen
### GET /
**Antwort**:  
```
{  
  "message": "KI-Agent läuft"  
}  
```
### POST /eintrag 
Beschreibung: Speichert einen neuen Chatverlaufseintrag in der Datenbank.  

**Beispielanfrage:**
```json
{  
  "benutzer": "Ayham",  
  "nachricht": "plane mir Ayham am Dienstag ein",  
  "timestamp": "2025-06-21 14:00:00"
} 
```

**Antwort:**
```
{  
  "status": "Eintrag gespeichert"  
}
```
### POST /chat
Beschreibung: Sendet eine Chat-Nachricht und erhält eine Antwort vom KI-Agenten.

**Beispielanfrage:**

```
{  
  "message": "Plane mir Gürhan am Mittwoch ein?"  
}
```
**Antwort:**
```
{  
  "response": "Gürhan wurde am 2025-07-16 eingeplant."  
}
```

### API-Dokumentation (Swagger UI):
Die vollständige automatisch generierte API-Dokumentation ist unter http://localhost:8000/docs verfügbar.



---

## Verwertungsplan
Dieses Projekt wurde im Rahmen des Moduls Softwareentwicklungsprojekt realisiert. Es dient als funktionaler Prototyp für eine mögliche spätere Integration in echte Planungssysteme. Die verwendete modulare Architektur erlaubt es, das System flexibel zu erweitern (z. B. automatische Vorschläge, externe Kalendersysteme, Reporting-Funktionen).

---

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der Datei `Lizenz`

---

## Kontakt
Bei Fragen oder Anmerkungen wenden Sie sich bitte an:

- Ayham.Salha@Student.HTW-Berlin.de;
- Guerhan.Arabaci@Student.HTW-Berlin.de;
- Koutaibe.Alhassan@Student.HTW-Berlin.de.

---