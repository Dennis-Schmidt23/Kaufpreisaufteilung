import pytest

from app.calculator.calculations.bodenanteil import (
    calculate_bodenanteil,
)

from app.models.input_data import InputData
from app.models.kaufvertrag import Kaufvertrag
from app.models.grundstueck import Grundstueck
from app.models.gebaeude import Gebaeude
from datetime import date
from tests.test_helpers import create_test_input


def create_data():

    data = create_test_input()

    data.kaufvertrag.kaufpreis = 500000
    data.gebaeudeanteil = 290000

    return data


def test_bodenanteil():

    data = create_data()

    result = calculate_bodenanteil(data)

    assert result == pytest.approx(210000.0)

def test_bodenanteil_ohne_gebaeudeanteil():

    data = create_data()

    data.gebaeudeanteil = None

    with pytest.raises(
        ValueError,
        match="Gebäudeanteil ist nicht gesetzt.",
    ):
        calculate_bodenanteil(data)