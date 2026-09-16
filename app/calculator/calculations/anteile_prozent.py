from app.models.input_data import InputData
import math


def calculate_bodenanteil_prozent(
        data: InputData,
    ) -> float:

        if data.gebaeudeanteil_prozent is None:
            raise ValueError(
                "Gebäudeanteil-Prozentsatz ist nicht gesetzt."
            )

        return 100 - data.gebaeudeanteil_prozent


def calculate_gebaeudeanteil_prozent(
    data: InputData,
) -> float:

    if data.bodenwert is None:
        raise ValueError(
            "Bodenwert ist nicht gesetzt."
        )

    if data.marktangepasster_sachwert is None:
        raise ValueError(
            "Marktangepasster Sachwert ist nicht gesetzt."
        )

    bodenwert = round(data.bodenwert)

    gebaeudeanteil_prozent = (
        100
        * (
            data.marktangepasster_sachwert
            - bodenwert
        )
        / data.marktangepasster_sachwert
    )


    return math.ceil(gebaeudeanteil_prozent * 100) / 100