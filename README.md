# 🚑 MediPlan – Digitaler Medikamentenplan

## Was ist MediPlan?
MediPlan ist eine Web-Anwendung für den Rettungsdienst, die ein häufiges Problem löst: 
Patienten wissen oft nicht welche Medikamente sie nehmen, Medipläne sind nicht aktuell 
oder gar nicht vorhanden. Im Notfall kostet das wertvolle Zeit.

Mit MediPlan kann jeder Patient seinen persönlichen Medikamentenplan digital pflegen. 
Ein QR-Code zum Ausdrucken (z.B. am Kühlschrank) ermöglicht dem Rettungsdienst 
im Notfall sofortigen Zugriff auf alle wichtigen Informationen.

## Funktionen
- 👤 Eigener Account pro Nutzer (Registrierung & Login)
- ➕ Patienten anlegen mit Name, Geburtsdatum und Allergien
- 💊 Medikamente mit Dosierung, Uhrzeit und Diagnose eintragen
- 📱 QR-Code generieren und ausdrucken
- 🗑️ Patienten und Medikamente löschen
- 🔒 Jeder Nutzer sieht nur seine eigenen Daten

## Technologien
- Python & Flask (Web-Framework)
- SQLite (Datenbank)
- Jinja2 (Templates)
- Bootstrap 5 (Design)
- qrcode (QR-Code Generierung)

## Installation
1. Repository klonen
2. Pakete installieren: `pip install flask qrcode[pil] werkzeug`
3. App starten: `python app.py`
4. Browser öffnen: `http://127.0.0.1:5000`

## Hintergrund
Dieses Projekt entstand im Rahmen des Moduls *Weiterführende Programmierkenntnisse* 
an der Hochschule Hamm-Lippstadt (HSHL) im Studiengang Biomedizinische Technologie.
Die Projektidee basiert auf realen Erfahrungen aus dem Rettungsdienst.