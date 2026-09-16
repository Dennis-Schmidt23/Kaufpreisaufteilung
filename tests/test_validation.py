import pytest

from app.calculator.validation import (
    validate,
    validate_kaufpreis,
    validate_grundstuecksflaeche,
    validate_bodenrichtwert,
    validate_bruttogrundflaeche,
    validate_gesamtnutzungsdauer,
    validate_anschaffungsjahr,
    validate_baujahr,
    validate_standardstufe,
    validate_nhk_code,
)
from datetime import date

from app.models.input_data import InputData
from app.models.kaufvertrag import Kaufvertrag
from app.models.grundstueck import Grundstueck
from app.models.gebaeude import Gebaeude


def create_valid_data():

    return InputData(
        kaufvertrag=Kaufvertrag(
            kaufpreis=500000,
            datum=date(2024, 1, 1),
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
        gesamtnutzungsdauer=80,
    )

# ---------------------------------------
# Kaufpreis
# ---------------------------------------

def test_validate_kaufpreis():

    data = create_valid_data()

    validate_kaufpreis(data)


def test_validate_kaufpreis_negativ():

    data = create_valid_data()

    data.kaufvertrag.kaufpreis = -1

    with pytest.raises(ValueError):
        validate_kaufpreis(data)

def test_validate_kaufpreis_null():

    data = create_valid_data()

    data.kaufvertrag.kaufpreis = 0

    with pytest.raises(ValueError):
        validate_kaufpreis(data)

# ---------------------------------------
# Grundstück
# ---------------------------------------

def test_validate_grundstuecksflaeche():

    data = create_valid_data()

    validate_grundstuecksflaeche(data)


def test_validate_grundstuecksflaeche_negativ():

    data = create_valid_data()

    data.grundstueck.flaeche_1 = -5

    with pytest.raises(ValueError):
        validate_grundstuecksflaeche(data)

def test_validate_grundstuecksflaeche_null():

    data = create_valid_data()

    data.grundstueck.flaeche_1 = 0

    with pytest.raises(ValueError):
        validate_grundstuecksflaeche(data)

def test_validate_bodenrichtwert():

    data = create_valid_data()

    validate_bodenrichtwert(data)


def test_validate_bodenrichtwert_negativ():

    data = create_valid_data()

    data.grundstueck.bodenrichtwert_1 = -10

    with pytest.raises(ValueError):
        validate_bodenrichtwert(data)

def test_validate_bodenrichtwert_null():

    data = create_valid_data()

    data.grundstueck.bodenrichtwert_1 = 0

    with pytest.raises(ValueError):
        validate_bodenrichtwert(data)

# ---------------------------------------
# Gebäude
# ---------------------------------------

def test_validate_bruttogrundflaeche():

    data = create_valid_data()

    validate_bruttogrundflaeche(data)


def test_validate_bruttogrundflaeche_null():

    data = create_valid_data()

    data.bruttogrundflaeche = 0

    with pytest.raises(ValueError):
        validate_bruttogrundflaeche(data)

def test_validate_bruttogrundflaeche_negativ():

    data = create_valid_data()

    data.bruttogrundflaeche = -10

    with pytest.raises(ValueError):
        validate_bruttogrundflaeche(data)

def test_validate_baujahr():

    data = create_valid_data()

    validate_baujahr(data)

def test_validate_baujahr_zu_klein():

    data = create_valid_data()

    data.gebaeude.baujahr = 1750

    with pytest.raises(ValueError):
        validate_baujahr(data)

def test_validate_gesamtnutzungsdauer():

    data = create_valid_data()

    validate_gesamtnutzungsdauer(data)


def test_validate_gesamtnutzungsdauer_null():

    data = create_valid_data()

    data.gesamtnutzungsdauer = 0

    with pytest.raises(ValueError):
        validate_gesamtnutzungsdauer(data)

def test_validate_gesamtnutzungsdauer_negativ():

    data = create_valid_data()

    data.gesamtnutzungsdauer = -1

    with pytest.raises(ValueError):
        validate_gesamtnutzungsdauer(data)

def test_validate_anschaffungsjahr():

    data = create_valid_data()

    validate_anschaffungsjahr(data)


def test_validate_anschaffungsjahr_vor_baujahr():

    data = create_valid_data()

    data.kaufvertrag.datum = date(1999, 1, 1)

    with pytest.raises(ValueError):
        validate_anschaffungsjahr(data)

def test_validate_anschaffungsjahr_zu_klein():

    data = create_valid_data()

    data.kaufvertrag.datum = date(1899, 1, 1)

    with pytest.raises(ValueError):
        validate_anschaffungsjahr(data)

# ---------------------------------------
# NHK
# ---------------------------------------

def test_validate_nhk_code():

    data = create_valid_data()

    validate_nhk_code(data)


def test_validate_nhk_code_leer():

    data = create_valid_data()

    data.nhk_code = ""

    with pytest.raises(ValueError):
        validate_nhk_code(data)

def test_validate_nhk_code_nur_leerzeichen():

    data = create_valid_data()

    data.nhk_code = "   "

    with pytest.raises(ValueError):
        validate_nhk_code(data)

def test_validate_standardstufe():

    data = create_valid_data()

    validate_standardstufe(data)

def test_validate_standardstufe_ungueltig():

    data = create_valid_data()

    data.standardstufe = 6

    with pytest.raises(ValueError):
        validate_standardstufe(data)

# ---------------------------------------
# Gesamtvalidierung
# ---------------------------------------

def test_validate():

    data = create_valid_data()

    validate(data)


def test_validate_mit_mehreren_fehlern():

    data = create_valid_data()

    data.kaufvertrag.kaufpreis = -100
    data.bruttogrundflaeche = 0

    with pytest.raises(ValueError):
        validate(data)

def test_validate_ungueltiger_bodenrichtwert():

    data = create_valid_data()

    data.grundstueck.bodenrichtwert_1 = -100

    with pytest.raises(ValueError):
        validate(data)

def test_engine_verwendet_validation():

    from app.calculator.engine import CalculationEngine

    data = create_valid_data()

    data.kaufvertrag.kaufpreis = -1

    with pytest.raises(ValueError):
        CalculationEngine().calculate(data)
