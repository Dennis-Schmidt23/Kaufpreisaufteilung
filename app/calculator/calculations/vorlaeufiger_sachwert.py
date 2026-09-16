from app.models.input_data import InputData


def calculate_vorlaeufiger_sachwert(
    data: InputData,
) -> float:

    if data.bodenwert is None:
        raise ValueError(
            "Bodenwert ist nicht gesetzt."
        )

    if data.gebaeudesachwert is None:
        raise ValueError(
            "Gebäudesachwert ist nicht gesetzt."
        )

    if data.garagenwert is None:
        raise ValueError(
            "Garagenwert ist nicht gesetzt."
        )

    return (
        data.bodenwert
        + data.gebaeudesachwert
        + data.garagenwert
    )