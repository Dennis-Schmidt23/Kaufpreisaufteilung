from pathlib import Path

from openpyxl import load_workbook


ROOT = Path(__file__).resolve().parent.parent
WORKBOOK = ROOT / "Kaufpreisaufteilung-Grundstuecke-Arbeitshilfe-Berechnung.xlsx"

wb = load_workbook(WORKBOOK, data_only=False)
ws = wb["KPA"]

print("Datenvalidierungen im Blatt 'KPA'")
print("-" * 60)

for dv in ws.data_validations.dataValidation:
    print(f"Bereich : {dv.sqref}")
    print(f"Typ     : {dv.type}")
    print(f"Formel1 : {dv.formula1}")
    print(f"Formel2 : {dv.formula2}")
    print("-" * 60)