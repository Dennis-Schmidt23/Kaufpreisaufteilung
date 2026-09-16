import json
from dataclasses import dataclass
from pathlib import Path
from functools import cache


@dataclass(frozen=True)
class NHKDatensatz:
    code: str
    gebaeudeart: str
    beschreibung: str

    nhk_1: float
    nhk_2: float
    nhk_3: float
    nhk_4: float
    nhk_5: float

    bgf_wohnflaeche_faktor: float
    gesamtnutzungsdauer: int

    def nhk_wert(
        self,
        standardstufe: int,
    ) -> float:

        if not 1 <= standardstufe <= 5:
            raise ValueError(
                "Die NHK-Stufe muss zwischen 1 und 5 liegen."
            )

        return getattr(
            self,
            f"nhk_{standardstufe}",
        )

@cache
def lade_nhk_daten() -> list[NHKDatensatz]:
    projekt_root = Path(__file__).resolve().parents[3]
    datei = projekt_root / "data" / "nhk.json"

    with datei.open(encoding="utf-8") as f:
        daten = json.load(f)

    return [
        NHKDatensatz(**datensatz)
        for datensatz in daten
    ]

def finde_nhk_datensatz(
    code: str,
    daten: list[NHKDatensatz] | None = None,
) -> NHKDatensatz:
    if daten is None:
        daten = lade_nhk_daten()

    for datensatz in daten:
        if datensatz.code == code:
            return datensatz

    raise ValueError(
        f"Kein NHK-Datensatz mit dem Code '{code}' gefunden."
    )

def nhk_form_options() -> list[dict[str, str]]:
    daten = lade_nhk_daten()

    return [
        {
            "value": datensatz.code,
            "label": (
                f"{datensatz.code} – "
                f"{datensatz.beschreibung}"
            ),
        }
        for datensatz in daten
    ]