from app.models.input_data import InputData


def calculate_alterswertminderung(
    data: InputData,
) -> float:

    if data.restnutzungsdauer is None:
        raise ValueError(
            "Restnutzungsdauer ist nicht gesetzt."
        )

    if data.gesamtnutzungsdauer is None:
        raise ValueError(
            "Gesamtnutzungsdauer ist nicht gesetzt."
        )

    if data.gesamtnutzungsdauer <= 0:
        raise ValueError(
            "Gesamtnutzungsdauer muss größer als 0 sein."
        )


    faktor = (
        data.restnutzungsdauer
        / data.gesamtnutzungsdauer
    )

    return max(faktor, 0.30)