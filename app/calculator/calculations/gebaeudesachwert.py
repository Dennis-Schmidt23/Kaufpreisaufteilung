from app.models.input_data import InputData
from app.calculator.calculations.aussenanlagen import (
    berechne_aussenanlagenpauschale,
)

def calculate_gebaeudesachwert(
    data: InputData,
) -> float:

    if data.normalherstellungskosten is None:
        raise ValueError(
            "Normalherstellungskosten ist nicht gesetzt."
        )

    if data.regionalfaktor is None:
        raise ValueError(
            "Regionalfaktor ist nicht gesetzt."
        )

    if data.alterswertminderung is None:
        raise ValueError(
            "Alterswertminderung ist nicht gesetzt."
        )

    if data.wohnflaeche is None:
        raise ValueError(
            "Wohnfläche ist nicht gesetzt."
        )

    aussenanlagenpauschale = berechne_aussenanlagenpauschale(
        data
    )

    wert_mit_aussenanlagen = round(
        data.normalherstellungskosten
        + aussenanlagenpauschale,
        0,
    )

    regionalangepasster_wert = round(
        wert_mit_aussenanlagen
        * data.regionalfaktor,
        0,
    )

    sachwert_je_qm = round(
        regionalangepasster_wert
        * data.alterswertminderung,
        0,
    )

    return round(
        sachwert_je_qm
        * round(data.wohnflaeche, 0),
        0,
    )