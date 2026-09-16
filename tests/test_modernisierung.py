import pytest

from app.calculator.calculations.modernisierung import (
    Modernisierung,
    calculate_modernisierungspunkte,
    punkte,
)
from datetime import date
from app.models.input_data import InputData
from app.models.kaufvertrag import Kaufvertrag
from app.models.grundstueck import Grundstueck
from app.models.gebaeude import Gebaeude
from datetime import date

def create_input_data():

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
            baujahr=2000,
        ),

        nhk_code="1.01",
        standardstufe=3,
        bruttogrundflaeche=190,

        dachmodernisierung=Modernisierung.NEIN,
        fenstermodernisierung=Modernisierung.NEIN,
        leitungsmodernisierung=Modernisierung.NEIN,
        heizungsmodernisierung=Modernisierung.NEIN,
        waermedaemmung=Modernisierung.NEIN,
        baedermodernisierung=Modernisierung.NEIN,
        innenausbau=Modernisierung.NEIN,
        grundriss=Modernisierung.NEIN,
    )


def test_ja():

    assert punkte(
        Modernisierung.JA,
        4,
    ) == 4


def test_teilweise():

    assert punkte(
        Modernisierung.TEILWEISE,
        4,
    ) == 2


def test_nein():

    assert punkte(
        Modernisierung.NEIN,
        4,
    ) == 0


def test_keine_modernisierung():

    data = create_input_data()

    assert (
        calculate_modernisierungspunkte(data)
        == 0
    )


def test_vollstaendig_modernisiert():

    data = create_input_data()

    data.dachmodernisierung = Modernisierung.JA
    data.fenstermodernisierung = Modernisierung.JA
    data.leitungsmodernisierung = Modernisierung.JA
    data.heizungsmodernisierung = Modernisierung.JA
    data.waermedaemmung = Modernisierung.JA
    data.baedermodernisierung = Modernisierung.JA
    data.innenausbau = Modernisierung.JA
    data.grundriss = Modernisierung.JA

    assert (
        calculate_modernisierungspunkte(data)
        == 20
    )


def test_gemischte_modernisierung():

    data = create_input_data()

    data.dachmodernisierung = Modernisierung.JA
    data.fenstermodernisierung = Modernisierung.TEILWEISE
    data.heizungsmodernisierung = Modernisierung.JA

    assert (
        calculate_modernisierungspunkte(data)
        == 7
    )