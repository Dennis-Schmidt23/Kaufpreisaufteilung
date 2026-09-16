from app.models.input_data import InputData


def calculate_bodenanteil(
    data: InputData,
) -> float:

    if data.gebaeudeanteil is None:
        raise ValueError(
            "Gebäudeanteil ist nicht gesetzt."
        )

    return (
        data.kaufvertrag.kaufpreis
        - data.gebaeudeanteil
    )