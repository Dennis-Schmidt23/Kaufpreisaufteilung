import pytest

from app.calculator.data.fiktives_baujahr import (
    FIKTIVE_BAUJAHR_PARAMETER,
    finde_parameter,
)


def test_alle_parameter_geladen():

    assert len(FIKTIVE_BAUJAHR_PARAMETER) == 18


def test_parameter_1_punkt():

    parameter = finde_parameter(1)

    assert parameter.modernisierungspunkte == 1
    assert parameter.a == 0.012500
    assert parameter.b == 2.625000
    assert parameter.c == 152.5000


def test_parameter_9_punkte():

    parameter = finde_parameter(9)

    assert parameter.modernisierungspunkte == 9
    assert parameter.a == 0.004660
    assert parameter.b == 1.027000
    assert parameter.c == 99.0560


def test_parameter_18_punkte():

    parameter = finde_parameter(18)

    assert parameter.modernisierungspunkte == 18
    assert parameter.a == 0.002000
    assert parameter.b == 0.440000
    assert parameter.c == 94.2000


def test_finde_parameter():

    parameter = finde_parameter(4)

    assert parameter.modernisierungspunkte == 4
    assert parameter.a == 0.007300
    assert parameter.b == 1.577000
    assert parameter.c == 111.3300


def test_mehr_als_18_punkte():

    parameter = finde_parameter(25)

    assert parameter.modernisierungspunkte == 18

def test_0_punkte_verwendet_parameter_1():

    parameter = finde_parameter(0)

    assert parameter.modernisierungspunkte == 1