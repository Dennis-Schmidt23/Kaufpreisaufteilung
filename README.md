# Kaufpreisaufteilung

Webanwendung zur Berechnung der Aufteilung eines Grundstückskaufpreises auf **Grund und Boden** sowie **Gebäude**.

Die Anwendung ist in Python mit FastAPI entwickelt und orientiert sich an der **Arbeitshilfe zur Aufteilung eines Grundstückskaufpreises** des Bundesministeriums der Finanzen (BMF).

> **Hinweis:** Das Projekt befindet sich noch in der Entwicklung. Die Berechnung dient der technischen Umsetzung und Nachbildung der zugrunde liegenden Berechnungslogik und stellt keine steuerliche Beratung dar.

---

## Funktionen

Die Anwendung unterstützt derzeit unter anderem:

- Erfassung des Kaufpreises
- Erfassung von Grundstücksfläche und Bodenrichtwert
- Berücksichtigung weiterer Grundstücksflächen und Bodenrichtwerte
- Berücksichtigung von Miteigentumsanteilen
- Auswahl der Gebäudeart bzw. des NHK-Typs
- Auswahl der Standardstufe
- Berechnung anhand der Normalherstellungskosten (NHK)
- Berücksichtigung des Baupreisindexes
- Berechnung des fiktiven Baujahres
- Berechnung der Restnutzungsdauer
- Berücksichtigung von Modernisierungsmaßnahmen
- Berechnung von Garagen- und Tiefgaragenwerten
- Berücksichtigung der Außenanlagenpauschale
- Berechnung des Gebäudesachwertes
- Berücksichtigung von Regionalfaktor und Sachwertfaktor
- Berechnung der Kaufpreisanteile für Grund und Boden sowie Gebäude
- Weboberfläche zur Eingabe der erforderlichen Daten
- umfangreiche automatisierte Tests

---

## Technischer Stack

- **Python**
- **FastAPI**
- **Jinja2**
- **Uvicorn**
- **pytest**
- HTML / CSS

---

## Voraussetzungen

Für die lokale Entwicklung werden benötigt:

- Python 3.14 oder eine kompatible Python-Version
- pip
- Git

---

## Installation

Repository klonen:

```bash
git clone https://github.com/Dennis-Schmidt23/Kaufpreisaufteilung
cd Kaufpreisaufteilung
```

Virtuelle Umgebung erstellen und aktivieren:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Falls die Aktivierung über PowerShell aufgrund der Execution Policy nicht möglich ist, kann alternativ die Eingabeaufforderung verwendet werden:

```bash
.venv\Scripts\activate.bat
```

Anschließend die benötigten Pakete installieren:

```bash
pip install -r requirements.txt
```

## Anwendung starten

Die FastAPI-Anwendung kann mit Uvicorn gestartet werden:

```bash
uvicorn app.main:app --reload
```

Anschließend ist die Anwendung lokal unter folgender Adresse erreichbar:

http://127.0.0.1:8000

## Tests

Die automatisierten Tests werden mit pytest ausgeführt:

```bash
pytest
```

Das Projekt enthält sowohl Unit-Tests für einzelne Berechnungskomponenten als auch Integrationstests für die vollständige Berechnungskette und die Webanwendung.

## Berechnungsgrundlage

Die Berechnungslogik orientiert sich an der Arbeitshilfe des Bundesministeriums der Finanzen zur Aufteilung eines Grundstückskaufpreises.

Insbesondere werden dabei unter anderem berücksichtigt:

Bodenwert
Normalherstellungskosten
Baupreisindex
Regionalfaktor
Alterswertminderung
Restnutzungsdauer
Modernisierungsmaßnahmen
Garagen und Tiefgaragen
Außenanlagenpauschale
Gebäudesachwert
Sachwertfaktor
marktangepasster Sachwert
Verhältnis von Boden- und Gebäudeanteil

Die im Projekt verwendeten Tabellen sind auf der offiziellen Seite des BMFs auffindbar.

## Referenzfälle

Zur Überprüfung der Berechnungslogik enthält das Projekt Referenzfälle unter:

```bash
tests/reference_cases/
```

Diese Fälle dienen dazu, Änderungen an der Berechnungslogik automatisiert gegen bereits definierte Ergebnisse zu überprüfen.

## Haftungsausschluss

Diese Software wird zu Entwicklungs- und Demonstrationszwecken bereitgestellt.

Die Ergebnisse ersetzen keine steuerliche, rechtliche oder sachverständige Beratung. Für die steuerliche Behandlung eines konkreten Grundstückskaufs sind die jeweils geltenden gesetzlichen Vorschriften, Verwaltungsanweisungen und die individuelle Sachverhaltsgestaltung maßgeblich.