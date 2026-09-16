import pytest
from app.calculator.calculations.gebaeudesachwert import (
    calculate_gebaeudesachwert,
)
from app.models.input_data import InputData
from app.models.kaufvertrag import Kaufvertrag
from app.models.grundstueck import Grundstueck
from app.models.gebaeude import Gebaeude
from app.calculator.data.baupreisindex import finde_baupreisindex
from app.calculator.data.nhk import finde_nhk_datensatz
from tests.test_helpers import create_test_input
from datetime import date

def test_gebaeudesachwert():

    data = create_test_input()
    data.normalherstellungskosten = 1531
    data.regionalfaktor = 1.0
    data.alterswertminderung = 0.3
    data.wohnflaeche = 190

    result = calculate_gebaeudesachwert(data)

    regionalangepasster_wert = round(
        1531 * 1.03,
        0,
    )

    sachwert_je_qm = round(
        regionalangepasster_wert * 0.3,
        0,
    )

    expected = round(
        sachwert_je_qm * round(190, 0),
        0,
    )


    assert result == expected

def test_gebaeudesachwert_ohne_normalherstellungskosten():

    data = create_test_input()

    data.normalherstellungskosten = None
    data.alterswertminderung = 0.8
    data.garagenwert = 0

    with pytest.raises(
        ValueError,
        match="Normalherstellungskosten ist nicht gesetzt.",
    ):
        calculate_gebaeudesachwert(data)


def test_gebaeudesachwert_ohne_alterswertminderung():

    data = create_test_input()

    data.normalherstellungskosten = 300000
    data.alterswertminderung = None
    data.garagenwert = 0

    with pytest.raises(
        ValueError,
        match="Alterswertminderung ist nicht gesetzt.",
    ):
        calculate_gebaeudesachwert(data)

def test_gebaeudesachwert_ohne_regionalfaktor():

    data = create_test_input()

    data.normalherstellungskosten = 300000
    data.regionalfaktor = None
    data.alterswertminderung = 0.45

    with pytest.raises(
        ValueError,
        match="Regionalfaktor ist nicht gesetzt.",
    ):
        calculate_gebaeudesachwert(data)

def test_gebaeudesachwert_ohne_wohnflaeche():

    data = create_test_input()

    data.normalherstellungskosten = 1531
    data.alterswertminderung = 0.3
    data.wohnflaeche = None

    with pytest.raises(
        ValueError,
        match="Wohnfläche ist nicht gesetzt.",
    ):
        calculate_gebaeudesachwert(data)

def test_gebaeudesachwert_rundung():

    data = create_test_input()

    data.normalherstellungskosten = 1234
    data.regionalfaktor = 1.087
    data.alterswertminderung = 0.73
    data.wohnflaeche = 190.4

    result = calculate_gebaeudesachwert(data)

    erwartete_nhk_mit_aussenanlagen = round(
        1234 * 1.03,
        0,
    )

    regionalangepasster_wert = round(
        erwartete_nhk_mit_aussenanlagen * 1.087,
        0,
    )

    sachwert_je_qm = round(
        regionalangepasster_wert * 0.73,
        0,
    )

    erwartete_wohnflaeche = round(
        190.4,
        0,
    )

    expected = round(
        sachwert_je_qm * erwartete_wohnflaeche,
        0,
    )


    assert result == expected