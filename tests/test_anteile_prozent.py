import pytest

from app.calculator.calculations.anteile_prozent import (
    calculate_bodenanteil_prozent,
    calculate_gebaeudeanteil_prozent,
)
from datetime import date
from tests.test_helpers import create_test_input


def create_data():

    data = create_test_input()

    data.kaufvertrag.kaufpreis = 500000
    data.bodenwert = 210000
    data.marktangepasster_sachwert = 300000
    data.gebaeudeanteil = 290000

    return data


def test_gebaeudeanteil_prozent():

    data = create_data()

    result = calculate_gebaeudeanteil_prozent(data)

    # (300.000 - 210.000) / 300.000 * 100
    # = 30,00 %
    assert result == pytest.approx(30.00)


def test_bodenanteil_prozent():

    data = create_data()

    # Gebäudeanteil = 30,00 %
    # Bodenanteil = 100 - 30,00
    data.gebaeudeanteil_prozent = (
        calculate_gebaeudeanteil_prozent(data)
    )

    result = calculate_bodenanteil_prozent(data)

    assert result == pytest.approx(70.00)

def test_gebaeudeanteil_prozent_ohne_bodenwert():

    data = create_data()
    data.bodenwert = None

    with pytest.raises(
        ValueError,
        match="Bodenwert ist nicht gesetzt.",
    ):
        calculate_gebaeudeanteil_prozent(data)

def test_gebaeudeanteil_prozent_ohne_marktangepassten_sachwert():

    data = create_data()
    data.marktangepasster_sachwert = None

    with pytest.raises(
        ValueError,
        match="Marktangepasster Sachwert ist nicht gesetzt.",
    ):
        calculate_gebaeudeanteil_prozent(data)

def test_bodenanteil_prozent_ohne_gebaeudeanteil_prozent():

    data = create_data()
    data.gebaeudeanteil_prozent = None

    with pytest.raises(
        ValueError,
        match="Gebäudeanteil-Prozentsatz ist nicht gesetzt.",
    ):
        calculate_bodenanteil_prozent(data)