from app.models.input_data import InputData


AUSSENANLAGEN_PAUSCHALE = 0.03


def berechne_aussenanlagenpauschale(
    data: InputData,
) -> float:
    """
    Berechnet die Außenanlagenpauschale.

    Die Außenanlagenpauschale beträgt 3 % der
    Normalherstellungskosten des Gebäudes.
    """

    return round(
        data.normalherstellungskosten
        * AUSSENANLAGEN_PAUSCHALE,
        0,
    )