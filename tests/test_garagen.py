import pytest
from datetime import date

from app.calculator.data.garagen import (
    EINZELGARAGE,
    TIEFGARAGE,
    berechne_kkw_einzelgarage,
    berechne_kkw_tiefgarage,
)
from app.calculator.data.baupreisindex import (
    finde_baupreisindex,
)


def test_einzelgarage_grunddaten():
    assert EINZELGARAGE.nhk_2010 == 485
    assert EINZELGARAGE.grundflaeche == pytest.approx(
        3 * 6 * 1.3
    )


def test_tiefgarage_grunddaten():
    assert TIEFGARAGE.nhk_2010 == 715
    assert TIEFGARAGE.grundflaeche == pytest.approx(
        7.5 * 2.3 * 1.1
    )


def test_kkw_einzelgarage():
    kkw = berechne_kkw_einzelgarage(
        datum=date(2024, 1, 1),
        regionalfaktor=0.95,
        alterswertminderungsfaktor=0.0375,
    )

    assert kkw == pytest.approx(
        741,
        abs=1,
    )


def test_kkw_tiefgarage():
    kkw = berechne_kkw_tiefgarage(
        datum=date(2024, 1, 1),
        regionalfaktor=0.95,
        alterswertminderungsfaktor=0.0375,
    )

    assert kkw == pytest.approx(
        886,
        abs=1,
    )

def test_kkw_garage_bmf_rundung():
    datum = date(2024, 1, 1)

    regionalfaktor = 1.0
    alterswertminderungsfaktor = 0.73

    result = berechne_kkw_einzelgarage(
        datum=datum,
        regionalfaktor=regionalfaktor,
        alterswertminderungsfaktor=alterswertminderungsfaktor,
    )

    baupreisindex = finde_baupreisindex(2024)

    kkw_2010 = round(
        EINZELGARAGE.nhk_2010
        * EINZELGARAGE.grundflaeche,
        0,
    )

    zwischenwert = round(
        kkw_2010
        * (baupreisindex.index / 100),
        0,
    )

    regionalangepasster_wert = round(
        zwischenwert * regionalfaktor,
        0,
    )

    expected = round(
        regionalangepasster_wert
        * alterswertminderungsfaktor,
        0,
    )

    assert result == expected