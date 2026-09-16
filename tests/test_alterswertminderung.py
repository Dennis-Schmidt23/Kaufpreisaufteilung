import pytest

from app.calculator.calculations.alterswertminderung import (
    calculate_alterswertminderung,
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

        restnutzungsdauer=36,
    )


def test_alterswertminderung():

    data = create_data()

    assert calculate_alterswertminderung(data) == 0.45


def test_neubau():

    data = create_data()

    data.restnutzungsdauer = 80

    assert calculate_alterswertminderung(data) == 1.0


def test_mindestrestwert():

    data = create_data()

    data.restnutzungsdauer = 0

    assert calculate_alterswertminderung(data) == 0.3

def test_restwert_unter_30_prozent():

    data = create_data()

    data.restnutzungsdauer = 20

    assert calculate_alterswertminderung(data) == 0.30

def test_restwert_genau_30_prozent():

    data = create_data()

    data.restnutzungsdauer = 24

    assert calculate_alterswertminderung(data) == 0.30

def test_restnutzungsdauer_fehlt():

    data = create_data()

    data.restnutzungsdauer = None

    with pytest.raises(ValueError):
        calculate_alterswertminderung(data)

def test_alterswertminderung_ohne_restnutzungsdauer():

    data = create_test_input()

    data.restnutzungsdauer = None

    with pytest.raises(
        ValueError,
        match="Restnutzungsdauer ist nicht gesetzt.",
    ):
        calculate_alterswertminderung(data)


def test_alterswertminderung_ohne_gesamtnutzungsdauer():

    data = create_test_input()

    # Alle vorherigen Voraussetzungen erfüllen
    data.restnutzungsdauer = 40

    # Den eigentlichen Fehler erzeugen
    data.gesamtnutzungsdauer = None

    with pytest.raises(
        ValueError,
        match="Gesamtnutzungsdauer ist nicht gesetzt.",
    ):
        calculate_alterswertminderung(data)

def test_alterswertminderung_gesamtnutzungsdauer_nicht_positiv():

    data = create_test_input()

    data.restnutzungsdauer = 40
    data.gesamtnutzungsdauer = 0

    with pytest.raises(
        ValueError,
        match="Gesamtnutzungsdauer muss größer als 0 sein.",
    ):
        calculate_alterswertminderung(data)