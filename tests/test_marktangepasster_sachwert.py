import pytest
from app.calculator.calculations.marktangepasster_sachwert import (
    calculate_marktangepasster_sachwert,
)
from tests.test_helpers import create_test_input
from datetime import date

def test_marktangepasster_sachwert_standard():

    data = create_test_input()

    data.vorlaeufiger_sachwert = 300000
    data.sachwertfaktor = 1.0

    assert (
        calculate_marktangepasster_sachwert(data)
        == 300000
    )

def test_marktangepasster_sachwert_kleiner_als_eins():

    data = create_test_input()

    data.vorlaeufiger_sachwert = 300000
    data.sachwertfaktor = 0.95

    assert (
        calculate_marktangepasster_sachwert(data)
        == 285000
    )

def test_marktangepasster_sachwert_groesser_als_eins():

    data = create_test_input()

    data.vorlaeufiger_sachwert = 300000
    data.sachwertfaktor = 1.15

    assert (
        calculate_marktangepasster_sachwert(data)
        == 345000
    )

def test_marktangepasster_sachwert_ohne_vorlaeufiger_sachwert():

    data = create_test_input()
    data.vorlaeufiger_sachwert = None
    data.sachwertfaktor = 1.0

    with pytest.raises(
        ValueError,
        match="Vorlaeufiger Sachwert ist nicht gesetzt.",
    ):
        calculate_marktangepasster_sachwert(data)


def test_marktangepasster_sachwert_ohne_sachwertfaktor():

    data = create_test_input()

    data.vorlaeufiger_sachwert = 250000
    data.sachwertfaktor = None

    with pytest.raises(
        ValueError,
        match="Sachwertfaktor ist nicht gesetzt.",
    ):
        calculate_marktangepasster_sachwert(data)

def test_marktangepasster_sachwert_rundet_sachwertfaktor():

    data = create_test_input()

    data.vorlaeufiger_sachwert = 300000
    data.sachwertfaktor = 1.23456

    result = calculate_marktangepasster_sachwert(data)

    assert result == 370380
