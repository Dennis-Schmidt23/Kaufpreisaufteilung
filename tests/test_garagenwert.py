import pytest

from app.calculator.calculations.garagenwert import (
    calculate_garagenwert,
)
from app.calculator.data.garagen import (
    berechne_kkw_einzelgarage,
    berechne_kkw_tiefgarage,
)
from tests.test_helpers import create_test_input
from datetime import date


def create_garagen_test_input(
    garagenstellplaetze=0,
    tiefgaragenstellplaetze=0,
):
    data = create_test_input(
        regionalfaktor=0.95,
        alterswertminderung=0.30,
    )

    data.gebaeude.garagenstellplaetze = (
        garagenstellplaetze
    )

    data.gebaeude.tiefgaragenstellplaetze = (
        tiefgaragenstellplaetze
    )

    return data


def test_garagenwert_ohne_stellplaetze():

    data = create_garagen_test_input()

    result = calculate_garagenwert(data)

    assert result == 0.0


def test_garagenwert_mit_einer_garage():

    data = create_garagen_test_input(
        garagenstellplaetze=1,
    )

    erwarteter_wert = (
        berechne_kkw_einzelgarage(
            datum=date(2024, 1, 1),
            regionalfaktor=0.95,
            alterswertminderungsfaktor=0.3,
        )
    )

    result = calculate_garagenwert(data)

    assert result == pytest.approx(
        erwarteter_wert
    )


def test_garagenwert_mit_zwei_garagen():

    data = create_garagen_test_input(
        garagenstellplaetze=2,
    )

    kkw = berechne_kkw_einzelgarage(
        datum=date(2024, 1, 1),
        regionalfaktor=0.95,
        alterswertminderungsfaktor=0.30,
    )

    result = calculate_garagenwert(data)

    assert result == pytest.approx(
        2 * kkw
    )


def test_garagenwert_mit_einem_tiefgaragenstellplatz():

    data = create_garagen_test_input(
        tiefgaragenstellplaetze=1,
    )

    erwarteter_wert = (
        berechne_kkw_tiefgarage(
            datum=date(2024, 1, 1),
            regionalfaktor=0.95,
            alterswertminderungsfaktor=0.30,
        )
    )

    result = calculate_garagenwert(data)

    assert result == pytest.approx(
        erwarteter_wert
    )


def test_garagenwert_mit_garage_und_tiefgarage():

    data = create_garagen_test_input(
        garagenstellplaetze=1,
        tiefgaragenstellplaetze=1,
    )

    garage_kkw = berechne_kkw_einzelgarage(
        datum=date(2024, 1, 1),
        regionalfaktor=0.95,
        alterswertminderungsfaktor=0.30,
    )

    tiefgarage_kkw = berechne_kkw_tiefgarage(
        datum=date(2024, 1, 1),
        regionalfaktor=0.95,
        alterswertminderungsfaktor=0.30,
    )

    erwarteter_wert = (
        garage_kkw
        + tiefgarage_kkw
    )

    result = calculate_garagenwert(data)

    assert result == pytest.approx(
        erwarteter_wert
    )


def test_garage_und_tiefgarage_haben_unterschiedliche_kkw():

    garage_kkw = berechne_kkw_einzelgarage(
        datum=date(2024, 1, 1),
        regionalfaktor=0.95,
        alterswertminderungsfaktor=0.3,
    )

    tiefgarage_kkw = berechne_kkw_tiefgarage(
        datum=date(2024, 1, 1),
        regionalfaktor=0.95,
        alterswertminderungsfaktor=0.3,
    )

    assert garage_kkw != tiefgarage_kkw

def test_kkw_einzelgarage():

    kkw = berechne_kkw_einzelgarage(
        datum=date(2024, 1, 1),
        regionalfaktor=0.95,
        alterswertminderungsfaktor=0.30,
    )

    kkw_2010 = 485 * (3 * 6 * 1.3)

    zwischenwert = round(
        kkw_2010 * (183.3 / 100),
        0,
    )

    regionalangepasster_wert = round(
        zwischenwert * 0.95,
        0,
    )

    erwartet = round(
        regionalangepasster_wert * 0.30,
        0,
    )

    assert kkw == erwartet
