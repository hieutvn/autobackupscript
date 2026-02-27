Python Backup Script Python Backup Script
---
Aufgabe:
  Ein einfaches Python-Skript zum Erstellen von Datei-Backups mit Zeitstempel.  

Ziel:
  - erlernen grundlegender Python Funktionen
  - Das Arbeiten mit Files und Ordner in Python
  - Das Zusammenstellen von Skripten für die Kommandozeile 
---

## Funktionen

- Sichert einen angegebenen Quellordner nach 24 Stunden
- Erstellt automatisch einen Backup-Ordner mit Zeitstempel
- Verhindert das Überschreiben alter Backups
- Optional als systemd-Service nutzbar
- Anfängerfreundlich und leicht erweiterbar

---

## Ordnerstruktur nach einem Backup

```
backups/
 ├── 27-02-2026_18-30-22/
 ├── 27-02-2026_19-30-22/
 └── 27-02-2026_20-30-22/
```

Jedes Backup erhält einen eigenen Zeitstempel.

---

## Voraussetzungen

- Python 3.8 oder höher
- Linux (empfohlen für Serverbetrieb)


## Verwendung

Auf dem Server:
- .service Konfiguartionsdatei erstellen
- Service aktivieren und starten
  -> sudo systemctl daemon-reload
  -> sudo systemctl enable backup.service
  -> sudo systemctl start backup.service

### Skript ausführen

```bash
python3 backup.py --source /pfad/zum/quellordner --destination backups
```

### Parameter

`--source` Ordner, welcher gesichert werden soll
`--destination` Zielordner für Backups (Standard: `backups`)
