from app.models.input_data import InputData
from app.models.kaufvertrag import Kaufvertrag
from app.models.grundstueck import Grundstueck
from app.models.gebaeude import Gebaeude
from datetime import date


def create_test_input(**kwargs):

    data = InputData(
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
            garagenstellplaetze=0,
            tiefgaragenstellplaetze=0,
        ),
        nhk_code="1.01",
        standardstufe=3,
        bruttogrundflaeche=190,
        wohnflaeche=190,
        gesamtnutzungsdauer=80,
        alterswertminderung=0.75,
    )

    for key, value in kwargs.items():
        setattr(data, key, value)

    return data