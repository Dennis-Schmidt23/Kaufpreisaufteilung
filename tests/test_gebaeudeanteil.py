import pytest

from app.calculator.calculations.gebaeudeanteil import (
    calculate_gebaeudeanteil,
)
from datetime import date
from app.models.input_data import InputData
from app.models.kaufvertrag import Kaufvertrag
from app.models.grundstueck import Grundstueck
from app.models.gebaeude import Gebaeude

from tests.test_helpers import create_test_input


def create_data():
    data = create_test_input()

    data.kaufvertrag.kaufpreis = 500000
    data.gebaeudeanteil_prozent = 58.0

    return data


def test_gebaeudeanteil():

    data = create_data()

    result = calculate_gebaeudeanteil(data)

    assert result == pytest.approx(290000.0)

def test_gebaeudeanteil_ohne_prozentwert():

    data = create_data()

    data.gebaeudeanteil_prozent = None

    with pytest.raises(
        ValueError,
        match="Gebäudeanteil-Prozentsatz ist nicht gesetzt.",
    ):
        calculate_gebaeudeanteil(data)