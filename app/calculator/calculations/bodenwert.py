from app.models.input_data import InputData


def calculate_bodenwert(data: InputData) -> float:

    grundstueck = data.grundstueck

    bodenwert = (
        round(grundstueck.flaeche_1, 0)
        * round(grundstueck.bodenrichtwert_1, 0)
        + round(grundstueck.flaeche_2, 0)
        * round(grundstueck.bodenrichtwert_2, 0)
    )

    if (
        grundstueck.miteigentumsanteil_zaehler is not None
        or grundstueck.miteigentumsanteil_nenner is not None
    ):

        if grundstueck.miteigentumsanteil_zaehler is None:
            raise ValueError(
                "Miteigentumsanteil-Zähler ist nicht gesetzt."
            )

        if grundstueck.miteigentumsanteil_nenner is None:
            raise ValueError(
                "Miteigentumsanteil-Nenner ist nicht gesetzt."
            )

        if grundstueck.miteigentumsanteil_nenner == 0:
            raise ValueError(
                "Miteigentumsanteil-Nenner darf nicht 0 sein."
            )

        bodenwert *= (
            grundstueck.miteigentumsanteil_zaehler
            / grundstueck.miteigentumsanteil_nenner
        )

    return round(bodenwert, 0)