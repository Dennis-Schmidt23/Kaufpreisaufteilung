from collections.abc import Mapping

from app.models.input_data import InputData
from app.models.kaufvertrag import Kaufvertrag
from app.models.grundstueck import Grundstueck
from app.models.gebaeude import Gebaeude
from datetime import date


def _optional_float(value):
    if value in (None, ""):
        return None
    return float(value)


def _optional_int(value):
    if value in (None, ""):
        return None
    return int(value)


def map_form_to_input_data(
    form: Mapping[str, str],
) -> InputData:

    kaufvertrag = Kaufvertrag(
        kaufpreis=float(form["kaufpreis"]),
        datum=date.fromisoformat(form["datum"]),
    )

    grundstueck = Grundstueck(
        flaeche_1=float(
            form["grundstuecksflaeche"]
        ),
        bodenrichtwert_1=float(
            form["bodenrichtwert"]
        ),
        flaeche_2=float(
            form.get("grundstuecksflaeche_2", 0)
        ),
        bodenrichtwert_2=float(
            form.get("bodenrichtwert_2", 0)
        ),
        miteigentumsanteil_zaehler=_optional_int(
            form.get("miteigentumsanteil_zaehler")
        ),
        miteigentumsanteil_nenner=_optional_int(
            form.get("miteigentumsanteil_nenner")
        ),
    )

    gebaeude = Gebaeude(
        baujahr=int(form["baujahr"]),
        garagenstellplaetze=int(
            form.get("garagenstellplaetze", 0)
        ),
        tiefgaragenstellplaetze=int(
            form.get("tiefgaragenstellplaetze", 0)
        ),
    )

    return InputData(
        kaufvertrag=kaufvertrag,
        grundstueck=grundstueck,
        gebaeude=gebaeude,

        wohnflaeche=_optional_float(
            form.get("wohnflaeche")
        ),

        nhk_code=form["nhk_code"],
        standardstufe=int(
            form["standardstufe"]
        ),

        bruttogrundflaeche=float(
            form["bruttogrundflaeche"]
        ),

        regionalfaktor=float(
            form.get(
                "regionalfaktor",
                1.0,
            )
        ),

        sachwertfaktor=float(
            form.get(
                "sachwertfaktor",
                1.0,
            )
        ),

        dachmodernisierung=form.get(
            "dachmodernisierung"
        ),
        fenstermodernisierung=form.get(
            "fenstermodernisierung"
        ),
        leitungsmodernisierung=form.get(
            "leitungsmodernisierung"
        ),
        heizungsmodernisierung=form.get(
            "heizungsmodernisierung"
        ),
        waermedaemmung=form.get(
            "waermedaemmung"
        ),
        baedermodernisierung=form.get(
            "baedermodernisierung"
        ),
        innenausbau=form.get(
            "innenausbau"
        ),
        grundriss=form.get(
            "grundriss"
        ),
    )