from app.models.input_data import InputData


def calculate_gebaeudeanteil(
    data: InputData,
) -> float:

    if data.gebaeudeanteil_prozent is None:
        raise ValueError(
            "Gebäudeanteil-Prozentsatz ist nicht gesetzt."
        )

    return (
        data.kaufvertrag.kaufpreis
        * data.gebaeudeanteil_prozent
        / 100
    )