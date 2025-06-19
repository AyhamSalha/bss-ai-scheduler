# KI-Agent für Personaleinsatzplanung (BSS)

## Projektvision

Ziel ist die Entwicklung eines intelligenten KI-gestützten Assistenzsystems, das Organisationsteams bei der Personaleinsatzplanung unterstützt. Der KI-Agent hilft, Einsatzpläne effizient zu erstellen, Fehler zu vermeiden und Mitarbeitende optimal einzusetzen – über eine benutzerfreundliche Chat-Oberfläche.

---

## Inhaltsverzeichnis

1. [Beschreibung](#beschreibung)
2. [Funktionen](#funktionen)
3. [Nicht-funktionale-Anforderungen](#nicht-funktionale-anforderungen)
4. [Systemanforderungen](#systemanforderungen)
5. [Externe-Schnittstellen](#externe-schnittstellen)
6. [Qualitätsanforderungen](#qualitätsanforderungen)
7. [Technologiestack](#technologiestack)
8. [Installation](#installation)
9. [Verwendung](#verwendung)
10. [Verwertungsplan](#verwertungsplan)
11. [Lizenz](#lizenz)
12. [Kontakt](#kontakt)

---

## Beschreibung

Das System ermöglicht die Planung über einen interaktiven Chat mit einem lokalen KI-Agenten.
Basierend auf Eingaben zu Verfügbarkeiten, Abwesenheiten, Qualifikationen und Mitarbeiterpräferenzen erstellt der Agent automatisch Vorschläge und zeigt Konflikte auf.

***Hauptmerkmale:***
- *Planung über Chat mit lokalem LLM (z. B. gemma:2b)*
- *Automatische Planungsvorschläge & Fehlererkennung*
- *Speicherung und Abruf des Chatverlaufs*
- *Verwaltung von Abwesenheiten & Einsatzwünschen*
- *Lokale Datenhaltung (SQLite)*

---

## Funktionen

### 1. Chatbasierte Planung mit KI-Agent  
Einsatzplanung direkt über eine Chat-Oberfläche.

### 2. Automatische Planungsvorschläge  
Vorschläge für geeignete Mitarbeitende und Schichten basierend auf Verfügbarkeit und Qualifikation.

### 3. Planungsfehler-Erkennung  
Automatisierte Erkennung von Konflikten (z. B. Überschneidungen, fehlende Qualifikationen).

### 4. Abwesenheitsverwaltung 
Erfassung von Ausfällen und individuellen Einsatzwünschen durch den Benutzer.

### 5. Verlaufsverwaltung 
Automatische Speicherung der Konversationen und Möglichkeit zum Abruf oder zur Löschung.

### 6. Planungsvorschau  
Übersicht über geplante Einsätze vor Freigabe.

---

## Nicht-funktionale Anforderungen
**Sicherheit:** Geschützte Kommunikation (HTTPS geplant), nur autorisierter Zugriff

**Wartbarkeit:** Modularer, dokumentierter Code mit Git-Versionierung

**Portabilität:** Plattformunabhängiger, lokaler Betrieb ohne Cloud-Zwang

**Kompatibilität:** Austauschbare KI-Modelle via REST-API

**Erweiterbarkeit:** Zukunftsfähig für Zusatzfunktionen wie Kalender oder Statistike

---

## Systemanforderungen

*Betriebssystem:*

- Windows, macOS, Linux

*Software:*

- Python 3.10 oder höher
- SQLite (lokal)
- Git
- Lokales LLM (z. B. gemma:2b)

---

## Externe Schnittstellen
- **Webbrowser (Frontend):** HTML, CSS, JS

- **REST-API (FastAPI):** JSON-basierte Schnittstelle

- **POST /chat** – Anfrage senden

- **GET /history** – Verlauf abrufen

- **Datenbank:** Speicherung von Anfragen, Antworten, Nutzerdaten

- **KI-Modell (z. B. gemma:2b):** Zugriff über lokale API
---

## Qualitätsanforderungen

• **Zuverlässigkeit**: >95 % korrekte Ergebnisse  
• **Antwortgeschwindigkeit**: <1 Sekunde bei 5 Anfragen gleichzeitig  
• **Skalierbarkeit**: bis zu 100 Mitarbeitende und 1000 Einsatzpläne/Jahr  
• **Benutzerfreundlichkeit**: responsives Design, klare Hinweise & Tooltips

---

## Technologiestack

• **Frontend**: HTML, CSS, JavaScript + Fetch API  
• **Backend/API**: FastAPI in Python  
• **Server**: Uvicorn (lokal)  
• **Datenbank**: SQLite (lokal)  
• **KI-Modell**: z. B. `gemma:2b` über Port 11434 (modular, lokal)  
• **Editor**: Visual Studio Code

---

## Installation

1. Stellen Sie sicher, dass Python (mindestens Version 3.10), Git und das lokale LLM (z. B. gemma:2b)
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
Öffnen Sie einen Webbrowser und rufen Sie http://localhost:8000 auf. Dort können Sie über die Chat-Oberfläche mit dem KI-Agenten interagieren, Einsatzpläne erstellen und verwalten. Das System analysiert Eingaben, prüft auf Konflikte und gibt passende Vorschläge aus.

---

## Verwertungsplan
Dieses Projekt wurde im Rahmen des Moduls Softwareentwicklungsprojekt realisiert. Es bietet eine Open-Source-Lösung zur lokalen, datenschutzkonformen Personaleinsatzplanung. Durch den modularen Aufbau kann es flexibel erweitert oder in bestehende Systeme integriert werden.

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