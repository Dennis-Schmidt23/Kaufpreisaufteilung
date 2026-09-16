import pytest

from app.calculator.calculations.fiktives_baujahr import (
    calculate_fiktives_baujahr,
)
from datetime import date
from app.models.input_data import InputData
from app.models.kaufvertrag import Kaufvertrag
from app.models.grundstueck import Grundstueck
from app.models.gebaeude import Gebaeude


def create_test_data():

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
        bruttogrundflaeche=230,

        gesamtnutzungsdauer=80,
        modernisierungspunkte=4,
    )


def test_fiktives_baujahr():

    data = create_test_data()

    result = calculate_fiktives_baujahr(data)

    assert isinstance(result, int)


def test_anschaffungsjahr_fehlt():

    data = create_test_data()

    data.kaufvertrag.datum = None

    with pytest.raises(ValueError):
        calculate_fiktives_baujahr(data)


def test_gesamtnutzungsdauer_fehlt():

    data = create_test_data()

    data.gesamtnutzungsdauer = None

    with pytest.raises(ValueError):
        calculate_fiktives_baujahr(data)


def test_modernisierungspunkte_fehlen():

    data = create_test_data()

    data.modernisierungspunkte = None

    with pytest.raises(ValueError):
        calculate_fiktives_baujahr(data)
