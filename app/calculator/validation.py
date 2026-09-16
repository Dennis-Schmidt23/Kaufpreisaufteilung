from app.models.input_data import InputData


def validate_kaufpreis(data: InputData):

    if data.kaufvertrag.kaufpreis <= 0:
        raise ValueError(
            "Der Kaufpreis muss größer als 0 sein."
        )


def validate_bruttogrundflaeche(data: InputData):

    if data.bruttogrundflaeche <= 0:
        raise ValueError(
            "Die Bruttogrundfläche muss größer als 0 sein."
        )


def validate_grundstuecksflaeche(data: InputData):

    if data.grundstueck.flaeche_1 <= 0:
        raise ValueError(
            "Die Grundstücksfläche muss größer als 0 sein."
        )


def validate_bodenrichtwert(data: InputData):

    if data.grundstueck.bodenrichtwert_1 <= 0:
        raise ValueError(
            "Der Bodenrichtwert muss größer als 0 sein."
        )

def validate_baujahr(data: InputData):

    if data.gebaeude.baujahr < 1800:
        raise ValueError(
            "Das Baujahr muss nach 1800 liegen."
        )


def validate_anschaffungsjahr(data: InputData):

    if (
        data.kaufvertrag.datum.year
        < data.gebaeude.baujahr
    ):
        raise ValueError(
            "Das Anschaffungsjahr darf nicht vor dem Baujahr liegen."
        )
    if data.kaufvertrag.datum.year < 1900:
        raise ValueError(
            "Das Anschaffungsjahr muss nach 1900 liegen."
        )


def validate_gesamtnutzungsdauer(data: InputData):

    if data.gesamtnutzungsdauer <= 0:
        raise ValueError(
            "Die Gesamtnutzungsdauer muss größer als 0 sein."
        )


def validate_nhk_code(data: InputData):

    if not data.nhk_code.strip():
        raise ValueError(
            "Der NHK-Code darf nicht leer sein."
        )

def validate_standardstufe(data: InputData):

    if data.standardstufe not in (1, 2, 3, 4, 5):
        raise ValueError(
            "Die Standardstufe muss zwischen 1 und 5 liegen."
        )


def validate(data: InputData):

    validate_kaufpreis(data)
    validate_grundstuecksflaeche(data)
    validate_bodenrichtwert(data)
    validate_bruttogrundflaeche(data)
    validate_gesamtnutzungsdauer(data)
    validate_baujahr(data)
    validate_standardstufe(data)
    validate_anschaffungsjahr(data)
    validate_nhk_code(data)