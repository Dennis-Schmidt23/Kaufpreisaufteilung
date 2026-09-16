from app.calculator.data.fiktives_baujahr import (
    finde_parameter,
)
from app.models.input_data import InputData


def calculate_fiktives_baujahr(data: InputData,) -> int:
    """
    Berechnet das fiktive Baujahr gemäß der
    BMF-Arbeitshilfe.

    Formel:

        fiktives Baujahr =
            round(
                a * Alter²
                - b * Alter
                + c * GND / 100
            )

    Alter = Anschaffungsjahr - Baujahr
    """

    if data.kaufvertrag.datum is None:
        raise ValueError(
            "Kaufvertragsdatum ist nicht gesetzt."
        )

    if data.gesamtnutzungsdauer is None:
        raise ValueError(
            "Gesamtnutzungsdauer ist nicht gesetzt."
        )

    if data.modernisierungspunkte is None:
        raise ValueError(
            "Modernisierungspunkte sind nicht gesetzt."
        )

    parameter = finde_parameter(
        data.modernisierungspunkte
    )

    alter = (
        data.kaufvertrag.datum.year
        - data.gebaeude.baujahr
    )

    fiktives_alter = round(
        parameter.a * alter ** 2
        - parameter.b * alter
        + (
            parameter.c
            * data.gesamtnutzungsdauer
            / 100
        )
    )

    fiktives_baujahr = (
        data.kaufvertrag.datum.year
        - fiktives_alter
    )

    return fiktives_baujahr