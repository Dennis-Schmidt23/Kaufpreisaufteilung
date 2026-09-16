from app.calculator.data.baupreisindex import (
    Baupreisindex,
)
from app.calculator.data.nhk import NHKDatensatz

def calculate_normalherstellungskosten(
        data: InputData,
        nhk: NHKDatensatz,
        baupreisindex: Baupreisindex,
    ) -> float:

    return round(
        nhk.nhk_wert(data.standardstufe)
        * (baupreisindex.index / 100),
        0,
    )