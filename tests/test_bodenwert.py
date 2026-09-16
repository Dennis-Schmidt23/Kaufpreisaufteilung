from app.calculator.calculations.bodenwert import calculate_bodenwert
from app.models.input_data import InputData
from app.models.kaufvertrag import Kaufvertrag
from app.models.grundstueck import Grundstueck
from app.models.gebaeude import Gebaeude
import pytest
from datetime import date

def create_test_data():
    print("create_test_data() wurde aufgerufen")
    return InputData(
        kaufvertrag=Kaufvertrag(
            kaufpreis=500000,
            datum=date(2024, 1, 1)
        ),

        grundstueck=Grundstueck(
            flaeche_1=600,
            bodenrichtwert_1=350,
        ),

        gebaeude=Gebaeude(
            baujahr=2000
        ),

        nhk_code="1.01",
        standardstufe=3,
        bruttogrundflaeche=190.0,
    )


def test_bodenwert():

    data = create_test_data()

    result = calculate_bodenwert(data)

    assert result == 210000

def test_bodenwert_mit_mehreren_flaechen():

    data = InputData(
        kaufvertrag=Kaufvertrag(
            kaufpreis=500000,
            datum=date(2024, 1, 1)
        ),

        grundstueck=Grundstueck(
            flaeche_1=600,
            bodenrichtwert_1=350,
            flaeche_2=100,
            bodenrichtwert_2=200,
        ),

        gebaeude=Gebaeude(
            baujahr=2000
        ),

        nhk_code="1.01",
        standardstufe=3,
        bruttogrundflaeche=190.0,
    )

    result = calculate_bodenwert(data)

    assert result == 230000

def test_bodenwert_rundet_eingabewerte():
    data = create_test_data()

    data.grundstueck.flaeche_1 = 600.6
    data.grundstueck.bodenrichtwert_1 = 350.4

    result = calculate_bodenwert(data)

    assert result == pytest.approx(
        round(600.6, 0) * round(350.4, 0)
    )

def test_bodenwert_ohne_miteigentumsanteil():

    data = create_test_data()

    data.grundstueck.miteigentumsanteil_zaehler = None
    data.grundstueck.miteigentumsanteil_nenner = None

    result = calculate_bodenwert(data)

    assert result == 210000

def test_bodenwert_miteigentumsanteil():

    data = create_test_data()

    data.grundstueck.miteigentumsanteil_zaehler = 1
    data.grundstueck.miteigentumsanteil_nenner = 2

    result = calculate_bodenwert(data)

    assert result == 105000

def test_bodenwert_miteigentumsanteil_drei_viertel():

    data = create_test_data()

    data.grundstueck.miteigentumsanteil_zaehler = 3
    data.grundstueck.miteigentumsanteil_nenner = 4

    result = calculate_bodenwert(data)

    assert result == 157500

def test_bodenwert_miteigentumsanteil_ohne_nenner():

    data = create_test_data()

    data.grundstueck.miteigentumsanteil_zaehler = 1
    data.grundstueck.miteigentumsanteil_nenner = None

    with pytest.raises(
        ValueError,
        match="Miteigentumsanteil-Nenner ist nicht gesetzt.",
    ):
        calculate_bodenwert(data)

def test_bodenwert_miteigentumsanteil_ohne_zaehler():

    data = create_test_data()

    data.grundstueck.miteigentumsanteil_zaehler = None
    data.grundstueck.miteigentumsanteil_nenner = 2

    with pytest.raises(
        ValueError,
        match="Miteigentumsanteil-Zähler ist nicht gesetzt.",
    ):
        calculate_bodenwert(data)

def test_bodenwert_miteigentumsanteil_nenner_null():

    data = create_test_data()

    data.grundstueck.miteigentumsanteil_zaehler = 1
    data.grundstueck.miteigentumsanteil_nenner = 0

    with pytest.raises(
        ValueError,
        match="Miteigentumsanteil-Nenner darf nicht 0 sein.",
    ):
        calculate_bodenwert(data)