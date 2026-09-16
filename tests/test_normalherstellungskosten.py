from app.calculator.calculations.normalherstellungskosten import (
    calculate_normalherstellungskosten,
)

from app.calculator.data.nhk import finde_nhk_datensatz
from app.calculator.data.baupreisindex import finde_baupreisindex

from app.models.input_data import InputData
from app.models.kaufvertrag import Kaufvertrag
from app.models.grundstueck import Grundstueck
from app.models.gebaeude import Gebaeude
from tests.test_helpers import create_test_input
from datetime import date

def test_normalherstellungskosten():

    data = InputData(
        kaufvertrag=Kaufvertrag(
            kaufpreis=500000,
            datum=date(2024, 1, 1),
        ),

        grundstueck=Grundstueck(
            flaeche_1=600,
            bodenrichtwert_1=350,
        ),

        gebaeude=Gebaeude(
            baujahr=2000,
        ),

        nhk_code="1.01",
        standardstufe=3,
        bruttogrundflaeche=190.0,

        gesamtnutzungsdauer=80,
    )

    nhk = finde_nhk_datensatz("1.01")
    index = finde_baupreisindex(2024)

    expected = (
        round(
            nhk.nhk_wert(3)
            * (index.index / 100),
            0
        )
        * 190

    )

    assert (
        calculate_normalherstellungskosten(
            data,
            nhk,
            index,
        )
        == expected
    )

def test_normalherstellungskosten():

    data = create_test_input()

    nhk = finde_nhk_datensatz(data.nhk_code)
    baupreisindex = finde_baupreisindex(
        data.kaufvertrag.datum.year
    )

    result = calculate_normalherstellungskosten(
        data,
        nhk,
        baupreisindex,
    )

    expected = round(
        nhk.nhk_wert(data.standardstufe)
        * (baupreisindex.index / 100),
        0,
    )

    assert result == expected
