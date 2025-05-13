# KI-Agent für Personaleinsatzplanung (BSS)

## 🧠 Projektübersicht

Ziel dieses Projekts ist die Entwicklung eines **KI-gestützten Assistenzsystems** zur Unterstützung der Personaleinsatzplanung.  
Ein intelligenter KI-Agent hilft dabei, Einsatzpläne effizient zu erstellen, Fehler zu vermeiden und Mitarbeitende optimal einzusetzen – interaktiv über eine Chat-Oberfläche.

---

## 🎯 Zielgruppe

• Führungskräfte in Unternehmen  
• Personalplaner*innen  
• Organisationsteams mit komplexen Schichtsystemen

---

## 🧩 Funktionen

### 1. Chatbasierte Planung mit KI-Agent  
Eingabe und Empfang von Nachrichten zur Personaleinsatzplanung über eine Weboberfläche.

### 2. Automatische Planungsvorschläge  
Vorschläge für geeignete Mitarbeitende und Schichten basierend auf Verfügbarkeit und Qualifikation.

### 3. Planungsfehler-Erkennung  
Automatisierte Erkennung von Konflikten (z. B. Überschneidungen, fehlende Qualifikationen).

### 4. Verwaltung von Abwesenheiten und Präferenzen  
Erfassung von Ausfällen und individuellen Einsatzwünschen durch den Benutzer.

### 5. Verlauf speichern, abrufen und löschen  
Automatische Speicherung der Konversationen und Möglichkeit zum Abruf oder zur Löschung.

### 6. Nutzung eines lokalen, modularen KI-Modells  
Lokaler Betrieb eines LLM (z. B. `gemma:2b`) über eine interne API – ohne Cloud-Abhängigkeit.

---

## ✅ Qualitätsanforderungen

• **Zuverlässigkeit**: >95 % korrekte Ergebnisse  
• **Antwortgeschwindigkeit**: <1 Sekunde bei 5 Anfragen gleichzeitig  
• **Skalierbarkeit**: bis zu 100 Mitarbeitende und 1000 Einsatzpläne/Jahr  
• **Benutzerfreundlichkeit**: responsives Design, klare Hinweise & Tooltips

---

## 🛠 Technologiestack

• **Frontend**: HTML, CSS, JavaScript + Fetch API  
• **Backend/API**: FastAPI in Python  
• **Server**: Uvicorn (lokal)  
• **Datenbank**: SQLite (lokal)  
• **KI-Modell**: z. B. `gemma:2b` über Port 11434 (modular, lokal)  
• **Editor**: Visual Studio Code

---

## ⚙️ Setup-Anleitung

### Voraussetzungen

• Python 3.10 oder höher  
• pip (Python-Paketmanager)  
• Git  
• Lokales LLM (z. B. `gemma:2b`) über Port 11434

### Installation

```bash
# Repository klonen
git clone https://gitlab.rz.htw-berlin.de/softwareentwicklungsprojekt/sose2025/team-14-personaleinsatzplanung-bss.git
cd team-14-personaleinsatzplanung-bss

```

## 👥 Teammitglieder

```text
Koutaibe Alhassan   – Kontext, Schnittstellen, Tech Stack
Gürhan Arabaci      – Use Cases, Datenmodell, Tests
Ayham Salha         – UI, Systemarchitektur, Qualitätsziele

---