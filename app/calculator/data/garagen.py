from dataclasses import dataclass

from app.calculator.data.baupreisindex import (
    finde_baupreisindex,
)
from datetime import date


@dataclass(frozen=True)
class GaragenDatensatz:
    bezeichnung: str
    grundflaeche: float
    nhk_2010: float


EINZELGARAGE = GaragenDatensatz(
    bezeichnung="Einzelgarage",
    grundflaeche=3 * 6 * 1.3,
    nhk_2010=485,
)


TIEFGARAGE = GaragenDatensatz(
    bezeichnung="Tiefgarage",
    grundflaeche=7.5 * 2.3 * 1.1,
    nhk_2010=715,
)


def berechne_kkw_garage(
    datensatz: GaragenDatensatz,
    datum: date,
    regionalfaktor: float,
    alterswertminderungsfaktor: float,
) -> float:

    baupreisindex = finde_baupreisindex(
        datum.year
    )

    kkw_2010 = round(
        datensatz.nhk_2010
        * datensatz.grundflaeche,
        0,
    )

    zwischenwert = round(
        kkw_2010
        * (baupreisindex.index / 100),
        0,
    )

    regionalangepasster_wert = round(
        zwischenwert
        * regionalfaktor,
        0,
    )

    kkw = round(
        regionalangepasster_wert
        * alterswertminderungsfaktor,
        0,
    )

    return kkw


def berechne_kkw_einzelgarage(
    datum: date,
    regionalfaktor: float,
    alterswertminderungsfaktor: float,
) -> float:

    return berechne_kkw_garage(
        datensatz=EINZELGARAGE,
        datum=datum,
        regionalfaktor=regionalfaktor,
        alterswertminderungsfaktor=alterswertminderungsfaktor,
    )


def berechne_kkw_tiefgarage(
    datum: date,
    regionalfaktor: float,
    alterswertminderungsfaktor: float,
) -> float:

    return berechne_kkw_garage(
        datensatz=TIEFGARAGE,
        datum=datum,
        regionalfaktor=regionalfaktor,
        alterswertminderungsfaktor=alterswertminderungsfaktor,
    )