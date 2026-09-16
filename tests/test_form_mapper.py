from app.form_mapper import map_form_to_input_data
from datetime import date

def test_map_form_to_input_data():

    form = {
        "kaufpreis": "500000",
        "datum": "2024-01-01",

        "grundstuecksflaeche": "600",
        "bodenrichtwert": "350",
        "grundstuecksflaeche_2": "200",
        "bodenrichtwert_2": "150",
        "miteigentumsanteil_zaehler": "1",
        "miteigentumsanteil_nenner": "2",

        "baujahr": "1998",
        "wohnflaeche": "145",

        "nhk_code": "1.01",
        "standardstufe": "3",

        "bruttogrundflaeche": "230",

        "garagenstellplaetze": "2",
        "tiefgaragenstellplaetze": "0",

        "regionalfaktor": "0.95",
        "sachwertfaktor": "1.05",

        "dachmodernisierung": "Umfassend",
        "fenstermodernisierung": "Teilweise",
        "leitungsmodernisierung": "Keine",
        "heizungsmodernisierung": "Teilweise",
        "waermedaemmung": "Keine",
        "baedermodernisierung": "Umfassend",
        "innenausbau": "Teilweise",
        "grundriss": "Keine",
    }

    data = map_form_to_input_data(form)

    # Kaufvertrag
    assert data.kaufvertrag.kaufpreis == 500000
    assert data.kaufvertrag.datum == date(2024, 1, 1)

    # Grundstück
    assert data.grundstueck.flaeche_1 == 600
    assert data.grundstueck.bodenrichtwert_1 == 350
    assert data.grundstueck.flaeche_2 == 200
    assert data.grundstueck.bodenrichtwert_2 == 150

    assert (
        data.grundstueck.miteigentumsanteil_zaehler
        == 1
    )
    assert (
        data.grundstueck.miteigentumsanteil_nenner
        == 2
    )

    # Gebäude
    assert data.gebaeude.baujahr == 1998
    assert data.gebaeude.garagenstellplaetze == 2
    assert data.gebaeude.tiefgaragenstellplaetze == 0

    # Gebäudedaten
    assert data.wohnflaeche == 145
    assert data.nhk_code == "1.01"
    assert data.standardstufe == 3
    assert data.bruttogrundflaeche == 230

    # Bewertungsparameter
    assert data.regionalfaktor == 0.95
    assert data.sachwertfaktor == 1.05

    # Modernisierung
    assert data.dachmodernisierung == "Umfassend"
    assert data.fenstermodernisierung == "Teilweise"
    assert data.leitungsmodernisierung == "Keine"
    assert data.heizungsmodernisierung == "Teilweise"
    assert data.waermedaemmung == "Keine"
    assert data.baedermodernisierung == "Umfassend"
    assert data.innenausbau == "Teilweise"
    assert data.grundriss == "Keine"