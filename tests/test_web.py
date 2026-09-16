from fastapi.testclient import TestClient
from app.form_mapper import map_form_to_input_data
from app.main import app


client = TestClient(app)


def test_calculate_route():
    response = client.post(
        "/calculate",
        data={
            # Kaufvertrag
            "kaufpreis": "500000",
            "datum": "2024-01-01",

            # Grundstück
            "grundstuecksflaeche": "600",
            "bodenrichtwert": "350",
            "grundstuecksflaeche_2": "200",
            "bodenrichtwert_2": "150",

            # Miteigentumsanteil
            "miteigentumsanteil_zaehler": "123",
            "miteigentumsanteil_nenner": "1000",

            # Gebäude
            "baujahr": "1998",
            "wohnflaeche": "145",
            "nhk_code": "1.01",
            "standardstufe": "3",
            "bruttogrundflaeche": "230",

            # Garagen
            "garagenstellplaetze": "2",
            "tiefgaragenstellplaetze": "0",

            # Bewertungsparameter
            "regionalfaktor": "0.95",
            "sachwertfaktor": "1.05",

            # Modernisierung
            "dachmodernisierung": "Umfassend",
            "fenstermodernisierung": "Teilweise",
            "leitungsmodernisierung": "Keine",
            "heizungsmodernisierung": "Teilweise",
            "waermedaemmung": "Keine",
            "baedermodernisierung": "Umfassend",
            "innenausbau": "Teilweise",
            "grundriss": "Keine",
        },
    )

    assert response.status_code == 200
    assert "Kaufpreisaufteilung" in response.text

def test_calculate_route_mit_zweiter_grundstuecksflaeche():
    response = client.post(
        "/calculate",
        data={
            "kaufpreis": "500000",
            "datum": "2024-01-01",

            "grundstuecksflaeche": "600",
            "bodenrichtwert": "350",
            "grundstuecksflaeche_2": "200",
            "bodenrichtwert_2": "150",

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
        },
    )

    assert response.status_code == 200
    assert "Kaufpreisaufteilung" in response.text

def test_map_form_to_input_data_mit_zweiter_grundstuecksflaeche():
    form = {
        "kaufpreis": "500000",
        "datum": "2024-01-01",

        "grundstuecksflaeche": "600",
        "bodenrichtwert": "350",

        "grundstuecksflaeche_2": "200",
        "bodenrichtwert_2": "150",

        "baujahr": "1998",
        "nhk_code": "1.01",
        "standardstufe": "3",
        "bruttogrundflaeche": "230",
    }

    data = map_form_to_input_data(form)

    assert data.grundstueck.flaeche_1 == 600
    assert data.grundstueck.bodenrichtwert_1 == 350

    assert data.grundstueck.flaeche_2 == 200
    assert data.grundstueck.bodenrichtwert_2 == 150

def test_map_form_to_input_data_mit_miteigentumsanteil():
    form = {
        "kaufpreis": "500000",
        "datum": "2024-01-01",

        "grundstuecksflaeche": "600",
        "bodenrichtwert": "350",

        "miteigentumsanteil_zaehler": "1",
        "miteigentumsanteil_nenner": "2",

        "baujahr": "1998",
        "nhk_code": "1.01",
        "standardstufe": "3",
        "bruttogrundflaeche": "230",
    }

    data = map_form_to_input_data(form)

    assert data.grundstueck.miteigentumsanteil_zaehler == 1
    assert data.grundstueck.miteigentumsanteil_nenner == 2

def test_calculate_route_mit_miteigentumsanteil():
    response = client.post(
        "/calculate",
        data={
            "kaufpreis": "500000",
            "datum": "2024-01-01",

            "grundstuecksflaeche": "600",
            "bodenrichtwert": "350",

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
        },
    )

    assert response.status_code == 200
    assert "Kaufpreisaufteilung" in response.text