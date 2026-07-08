# 🚑 MediPlan – Digitaler Medikamentenplan

> ❤️‍🩹 Ein aktueller, vollständiger Medikamentenplan kann Leben retten.

## Das Problem
Medikamentenpläne sind im Notfall oft nicht aktuell, nicht auffindbar oder gar nicht 
vorhanden. Patienten wissen häufig nicht welche Medikamente sie nehmen oder können 
diese Information im Notfall nicht mitteilen — gerade ältere Menschen sind hier oft 
auf Unterstützung angewiesen. Für den Rettungsdienst kostet das wertvolle Zeit.

Ein weiteres Problem: Selbst wenn ein Mediplan vorhanden ist, muss er erst gefunden 
werden. Liegt er bei jedem woanders, verliert der Rettungsdienst im Notfall kostbare 
Sekunden beim Suchen.

## Die Lösung
Mit MediPlan können Patienten oder ihre Angehörigen den persönlichen Medikamentenplan 
einfach digital pflegen. Ein QR-Code wird ausgedruckt und **fest am Kühlschrank** 
befestigt — einem Ort den der Rettungsdienst standardmäßig als ersten Anlaufpunkt kennt. 
Im Notfall einfach scannen und sofort alle wichtigen Informationen im Blick.

## Funktionen
- 👤 Eigener Account pro Nutzer (Registrierung & Login)
- ➕ Patienten anlegen mit Name, Geburtsdatum und Allergien
- ✏️ Patienten nachträglich bearbeiten
- 💊 Medikamente mit Dosierung, Uhrzeit und Diagnose eintragen & löschen
- 📞 Notfallkontakt hinterlegen
- 🩺 Hausarzt mit Telefonnummer hinterlegen
- 📱 QR-Code generieren und am Kühlschrank ausdrucken
- 🔒 Jeder Nutzer sieht nur seine eigenen Daten

## Technologien
- Python & Flask (Web-Framework)
- SQLite (Datenbank)
- Jinja2 (Templates)
- Bootstrap 5 (Design)
- qrcode (QR-Code Generierung)
- werkzeug (Passwort-Sicherheit)

## Installation
1. Repository klonen
2. Pakete installieren: `pip install flask qrcode[pil] werkzeug`
3. App starten: `python app.py`
4. Browser öffnen: `http://127.0.0.1:5000`

## Hintergrund
Dieses Projekt entstand im Rahmen des Moduls *Weiterführende Programmierkenntnisse* 
an der Hochschule Hamm-Lippstadt (HSHL) im Studiengang Biomedizinische Technologie.
Die Projektidee basiert auf realen Erfahrungen aus dem Rettungsdienst.