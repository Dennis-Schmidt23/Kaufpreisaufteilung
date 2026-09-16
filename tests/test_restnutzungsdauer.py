import pytest

from app.calculator.calculations.restnutzungsdauer import (
    calculate_restnutzungsdauer,
)
from datetime import date
from app.models.input_data import InputData
from app.models.kaufvertrag import Kaufvertrag
from app.models.grundstueck import Grundstueck
from app.models.gebaeude import Gebaeude
from tests.test_helpers import create_test_input

def create_data():

    return InputData(
        kaufvertrag=Kaufvertrag(
            kaufpreis=500000,
            datum=date(2024, 1, 1),
        ),

        grundstueck=Grundstueck(
            flaeche_1=600,
            bodenrichtwert_1=350,
        ),

        gebaeude=Gebaeude(
            baujahr=1975,
        ),

        nhk_code="1.01",
        standardstufe=3,
        bruttogrundflaeche=190.0,
        gesamtnutzungsdauer=80,

        fiktives_baujahr=1980,
    )


def test_restnutzungsdauer():

    data = create_data()

    assert (
        calculate_restnutzungsdauer(data)
        == 36
    )


def test_gebaeudealter_0():

    data = create_data()

    data.fiktives_baujahr = 2024

    assert (
        calculate_restnutzungsdauer(data)
        == 80
    )


def test_restnutzungsdauer_0():

    data = create_data()

    data.fiktives_baujahr = 1900

    assert (
        calculate_restnutzungsdauer(data)
        == 0
    )


def test_fiktives_baujahr_fehlt():

    data = create_data()

    data.fiktives_baujahr = None

    with pytest.raises(ValueError):
        calculate_restnutzungsdauer(data)



def test_restnutzungsdauer_ohne_gesamtnutzungsdauer():

    data = create_test_input()

    data.gesamtnutzungsdauer = None

    with pytest.raises(
        ValueError,
        match="Gesamtnutzungsdauer ist nicht gesetzt.",
    ):
        calculate_restnutzungsdauer(data)

import pytest

from app.calculator.calculations.restnutzungsdauer import (
    calculate_restnutzungsdauer,
)
from tests.test_helpers import create_test_input


def test_restnutzungsdauer_ohne_fiktives_baujahr():

    data = create_test_input()

    data.fiktives_baujahr = None
    data.gesamtnutzungsdauer = 80

    with pytest.raises(
        ValueError,
        match="Fiktives Baujahr ist nicht gesetzt.",
    ):
        calculate_restnutzungsdauer(data)

def test_restnutzungsdauer_ohne_datum():

    data = create_test_input()

    data.kaufvertrag.datum = None
    data.gesamtnutzungsdauer = 80
    data.fiktives_baujahr = 1990

    with pytest.raises(
        ValueError,
        match="Kaufvertragsdatum ist nicht gesetzt.",
    ):
        calculate_restnutzungsdauer(data)