import pytest

from app.calculator.calculations.vorlaeufiger_sachwert import (
    calculate_vorlaeufiger_sachwert,
)

from app.models.input_data import InputData
from app.models.kaufvertrag import Kaufvertrag
from app.models.grundstueck import Grundstueck
from app.models.gebaeude import Gebaeude
from datetime import date


def create_data():

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
        bruttogrundflaeche=190,
        gesamtnutzungsdauer=80,
    )

    data.bodenwert = 210000
    data.gebaeudesachwert = 280000
    data.garagenwert = 10000

    return data


def test_vorlaeufiger_sachwert():

    data = create_data()

    result = calculate_vorlaeufiger_sachwert(data)

    assert result == 500000


def test_fehler_ohne_bodenwert():

    data = create_data()

    data.bodenwert = None

    with pytest.raises(ValueError):

        calculate_vorlaeufiger_sachwert(data)


def test_fehler_ohne_gebaeudesachwert():

    data = create_data()

    data.gebaeudesachwert = None

    with pytest.raises(ValueError):

        calculate_vorlaeufiger_sachwert(data)

def test_fehler_ohne_garagenwert():

    data = create_data()

    data.garagenwert = None

    with pytest.raises(
        ValueError,
        match="Garagenwert ist nicht gesetzt.",
    ):
        calculate_vorlaeufiger_sachwert(data)