from app.models.input_data import InputData

from app.calculator.data.garagen import (
    berechne_kkw_einzelgarage,
    berechne_kkw_tiefgarage,
)


def calculate_garagenwert(
    data: InputData,
) -> float:

    if data.gebaeude is None:
        raise ValueError(
            "Gebäude ist nicht gesetzt."
        )

    if data.kaufvertrag.datum is None:
        raise ValueError(
            "Kaufvertragsdatum ist nicht gesetzt."
        )

    if data.alterswertminderung is None:
        raise ValueError(
            "Alterswertminderung ist nicht gesetzt."
        )

    garagen = (
        data.gebaeude.garagenstellplaetze
    )

    tiefgaragen = (
        data.gebaeude.tiefgaragenstellplaetze
    )

    if garagen == 0 and tiefgaragen == 0:
        return 0.0

    garage_kkw = berechne_kkw_einzelgarage(
        datum=data.kaufvertrag.datum,
        regionalfaktor=data.regionalfaktor,
        alterswertminderungsfaktor=data.alterswertminderung,
    )

    tiefgarage_kkw = berechne_kkw_tiefgarage(
        datum=data.kaufvertrag.datum,
        regionalfaktor=data.regionalfaktor,
        alterswertminderungsfaktor=data.alterswertminderung,
    )

    return (
        garagen * garage_kkw
        + tiefgaragen * tiefgarage_kkw
    )