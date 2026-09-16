import pytest
import math
from app.models.kaufvertrag import Kaufvertrag
from app.models.grundstueck import Grundstueck
from app.models.gebaeude import Gebaeude
from app.calculator.engine import CalculationEngine
from app.models.input_data import InputData
from app.calculator.data.baupreisindex import finde_baupreisindex
from app.calculator.data.nhk import finde_nhk_datensatz
from datetime import date


def test_bodenwert():
    daten = InputData(
    kaufvertrag=Kaufvertrag(
        kaufpreis=500000,
        datum=date(2024, 1, 1)
    ),

    grundstueck=Grundstueck(
        flaeche_1=600,
        bodenrichtwert_1=350,
        miteigentumsanteil_zaehler=1,
        miteigentumsanteil_nenner=2,
    ),

    gebaeude=Gebaeude(
        baujahr=2000
    ),

    nhk_code="1.01",
    standardstufe=3,
    bruttogrundflaeche=190.0,
    wohnflaeche=190.0,
    gesamtnutzungsdauer=80,

)


    nhk = finde_nhk_datensatz("1.01")
    index = finde_baupreisindex(2024)
    engine = CalculationEngine()

    result = engine.calculate(daten)

    expected_normalherstellungskosten = round(
        nhk.nhk_wert(3)
        * (index.index / 100),
        0
    )

    assert result.bodenwert == 105000

    assert result.bodenanteil == pytest.approx(
        daten.kaufvertrag.kaufpreis
        - result.gebaeudeanteil
    )

    assert (
        result.normalherstellungskosten
        == expected_normalherstellungskosten
    )

    expected_nhk_mit_aussenanlagen = round(
        expected_normalherstellungskosten * 1.03,
        0,
    )

    expected_regionalangepasster_wert = round(
        expected_nhk_mit_aussenanlagen
        * daten.regionalfaktor,
        0,
    )

    expected_sachwert_je_qm = round(
        expected_regionalangepasster_wert
        * result.alterswertminderung,
        0,
    )

    expected_gebaeudesachwert = round(
        expected_sachwert_je_qm
        * daten.bruttogrundflaeche,
        0,
    )


    assert result.gebaeudesachwert == expected_gebaeudesachwert

    assert result.fiktives_baujahr == 1958

    expected_gebaeudeanteil = (
        daten.kaufvertrag.kaufpreis
        * result.gebaeudeanteil_prozent
        / 100
    )

    expected_bodenanteil = (
        daten.kaufvertrag.kaufpreis
        - expected_gebaeudeanteil
    )

    assert result.gebaeudeanteil == pytest.approx(
        expected_gebaeudeanteil
    )

    assert result.bodenanteil == pytest.approx(
        expected_bodenanteil
    )

    expected_gebaeudeanteil_prozent = (
        100
        * (
            result.marktangepasster_sachwert
            - result.bodenwert
        )
        / result.marktangepasster_sachwert
    )

    expected_gebaeudeanteil_prozent = (
        math.ceil(
            expected_gebaeudeanteil_prozent * 100
        )
        / 100
    )

    expected_bodenanteil_prozent = (
        100 - expected_gebaeudeanteil_prozent
    )

    assert result.gebaeudeanteil_prozent == pytest.approx(
        expected_gebaeudeanteil_prozent
    )

    assert result.bodenanteil_prozent == pytest.approx(
        expected_bodenanteil_prozent
    )

    assert result.garagenwert >= 0
    assert result.sachwertfaktor == 1.0


def test_calculation_engine_komplette_kette():

    daten = InputData(
        kaufvertrag=Kaufvertrag(
            kaufpreis=500000,
            datum=date(2024, 1, 1)
        ),

        grundstueck=Grundstueck(
            flaeche_1=600,
            bodenrichtwert_1=350,
            miteigentumsanteil_zaehler=1,
            miteigentumsanteil_nenner=2,
        ),

        gebaeude=Gebaeude(
            baujahr=2000
        ),

        nhk_code="1.01",
        standardstufe=3,
        bruttogrundflaeche=190.0,
        wohnflaeche=190.0,
        gesamtnutzungsdauer=80,
    )

    engine = CalculationEngine()
    nhk = finde_nhk_datensatz("1.01")

    result = engine.calculate(daten)

    # Grund und Boden
    assert result.bodenwert == 105000

    # Gebäude
    assert result.normalherstellungskosten == pytest.approx(1531)

    expected_nhk_mit_aussenanlagen = round(
        daten.normalherstellungskosten * 1.03,
        0,
    )
    regionalangepasster_wert = round(
        expected_nhk_mit_aussenanlagen
        * daten.regionalfaktor,
        0,
    )

    sachwert_je_qm = round(
        regionalangepasster_wert
        * result.alterswertminderung,
        0,
    )

    expected_gebaeudesachwert = round(
        sachwert_je_qm
        * daten.bruttogrundflaeche,
        0,
    )

    assert result.gebaeudesachwert == pytest.approx(
        expected_gebaeudesachwert
    )

    # Sachwert
    assert result.vorlaeufiger_sachwert == pytest.approx(
        result.bodenwert
        + result.gebaeudesachwert
        + result.garagenwert
    )

    assert result.marktangepasster_sachwert == pytest.approx(
        result.vorlaeufiger_sachwert
        * round(result.sachwertfaktor, 4)
    )

    # Kaufpreisaufteilung
    assert result.gebaeudeanteil_prozent == pytest.approx(
        46.12
    )

    assert result.bodenanteil_prozent == pytest.approx(
        53.88
    )

    assert result.gebaeudeanteil == pytest.approx(
        daten.kaufvertrag.kaufpreis
        * result.gebaeudeanteil_prozent
        / 100
    )

    assert result.bodenanteil == pytest.approx(
        daten.kaufvertrag.kaufpreis
        - result.gebaeudeanteil
    )

    # Wichtigste Gesamtprüfung
    assert (
        result.gebaeudeanteil
        + result.bodenanteil
        == pytest.approx(
            daten.kaufvertrag.kaufpreis
        )
    )

def test_calculation_engine_aussenanlagenpauschale():
    daten = InputData(
        kaufvertrag=Kaufvertrag(
            kaufpreis=500000,
            datum=date(2024, 1, 1),
        ),

        grundstueck=Grundstueck(
            flaeche_1=600,
            bodenrichtwert_1=350,
            miteigentumsanteil_zaehler=1,
            miteigentumsanteil_nenner=2,
        ),

        gebaeude=Gebaeude(
            baujahr=2000,
        ),

        nhk_code="1.01",
        standardstufe=3,
        bruttogrundflaeche=190.0,
        wohnflaeche=190.0,
        gesamtnutzungsdauer=80,
    )

    engine = CalculationEngine()
    result = engine.calculate(daten)

    # NHK ohne Außenanlagenpauschale
    nhk_ohne_aussenanlagen = result.normalherstellungskosten

    # 3-%-Außenanlagenpauschale
    erwartete_nhk_mit_aussenanlagen = round(
        nhk_ohne_aussenanlagen * 1.03,
        0,
    )

    # Weitere Berechnung entsprechend der Gebäudesachwertberechnung
    regionalangepasster_wert = round(
        erwartete_nhk_mit_aussenanlagen
        * daten.regionalfaktor,
        0,
    )

    sachwert_je_qm = round(
        regionalangepasster_wert
        * result.alterswertminderung,
        0,
    )

    erwarteter_gebaeudesachwert = round(
        sachwert_je_qm
        * daten.bruttogrundflaeche,
        0,
    )

    assert result.gebaeudesachwert == pytest.approx(
        erwarteter_gebaeudesachwert
    )

    # Kontrolle: Ohne Außenanlagenpauschale wäre der Gebäudesachwert niedriger.
    sachwert_ohne_aussenanlagen = round(
        round(
            nhk_ohne_aussenanlagen
            * daten.regionalfaktor,
            0,
        )
        * result.alterswertminderung,
        0,
    )

    erwarteter_gebaeudesachwert_ohne_aussenanlagen = round(
        sachwert_ohne_aussenanlagen
        * daten.bruttogrundflaeche,
        0,
    )

    assert result.gebaeudesachwert > (
        erwarteter_gebaeudesachwert_ohne_aussenanlagen
    )

    print("Bodenwert:", result.bodenwert)
    print("Gebäudesachwert:", result.gebaeudesachwert)
    print("Garagenwert:", result.garagenwert)
    print("Vorläufiger Sachwert:", result.vorlaeufiger_sachwert)
    print("Sachwertfaktor:", result.sachwertfaktor)
    print("Marktangepasster Sachwert:", result.marktangepasster_sachwert)
    print("Gebäudeanteil %:", result.gebaeudeanteil_prozent)
