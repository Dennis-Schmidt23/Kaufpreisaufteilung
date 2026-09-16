import pytest
from app.calculator.data.nhk import (
    NHKDatensatz,
    lade_nhk_daten,
    finde_nhk_datensatz,
)


def test_alle_nhk_daten_aus_bmf_importiert():
    daten = lade_nhk_daten()

    assert len(daten) == 48


def test_nhk_datensatz_1_01():
    datensatz = finde_nhk_datensatz("1.01")

    assert datensatz.nhk_1 == 655
    assert datensatz.nhk_2 == 725
    assert datensatz.nhk_3 == 835
    assert datensatz.nhk_4 == 1005
    assert datensatz.nhk_5 == 1260

    assert datensatz.bgf_wohnflaeche_faktor == 2.3
    assert datensatz.gesamtnutzungsdauer == 80


def test_unbekannter_nhk_code():
    with pytest.raises(ValueError):
        finde_nhk_datensatz("NICHT_VORHANDEN")


def test_ungueltige_nhk_stufe():
    datensatz = NHKDatensatz(
        code="1.01",
        gebaeudeart="Einfamilienhaus",
        beschreibung="Test",
        nhk_1=655,
        nhk_2=725,
        nhk_3=835,
        nhk_4=1005,
        nhk_5=1260,
        bgf_wohnflaeche_faktor=2.3,
        gesamtnutzungsdauer=80,
    )

    with pytest.raises(ValueError):
        datensatz.nhk_wert(6)

def test_nhk_datensatz():
    datensatz = NHKDatensatz(
        code="1.01",
        gebaeudeart="Testgebäude",
        beschreibung="Testbeschreibung",
        nhk_1=655,
        nhk_2=725,
        nhk_3=835,
        nhk_4=1005,
        nhk_5=1260,
        bgf_wohnflaeche_faktor=2.3,
        gesamtnutzungsdauer=80,
    )

    assert datensatz.code == "1.01"
    assert datensatz.gebaeudeart == "Testgebäude"
    assert datensatz.beschreibung == "Testbeschreibung"

    assert datensatz.nhk_1 == 655
    assert datensatz.nhk_2 == 725
    assert datensatz.nhk_3 == 835
    assert datensatz.nhk_4 == 1005
    assert datensatz.nhk_5 == 1260

    assert datensatz.bgf_wohnflaeche_faktor == 2.3
    assert datensatz.gesamtnutzungsdauer == 80

def test_nhk_wert_aus_standardstufe():
    datensatz = NHKDatensatz(
        code="1.01",
        gebaeudeart="Einfamilienhaus",
        beschreibung="Test",
        nhk_1=655,
        nhk_2=725,
        nhk_3=835,
        nhk_4=1005,
        nhk_5=1260,
        bgf_wohnflaeche_faktor=2.3,
        gesamtnutzungsdauer=80,
    )

    assert datensatz.nhk_wert(1) == 655
    assert datensatz.nhk_wert(3) == 835
    assert datensatz.nhk_wert(5) == 1260
