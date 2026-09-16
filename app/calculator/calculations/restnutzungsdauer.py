from app.models.input_data import InputData


def calculate_restnutzungsdauer(
    data: InputData,
) -> int:

    if data.kaufvertrag.datum is None:
        raise ValueError(
            "Kaufvertragsdatum ist nicht gesetzt."
        )

    if data.gesamtnutzungsdauer is None:
        raise ValueError(
            "Gesamtnutzungsdauer ist nicht gesetzt."
        )

    if data.fiktives_baujahr is None:
        raise ValueError(
            "Fiktives Baujahr ist nicht gesetzt."
        )

    gebaeudealter = (
        data.kaufvertrag.datum.year
        - data.fiktives_baujahr
    )

    restnutzungsdauer = (
        data.gesamtnutzungsdauer
        - gebaeudealter
    )

    if restnutzungsdauer < 0:
        restnutzungsdauer = 0

    return int(round(restnutzungsdauer))