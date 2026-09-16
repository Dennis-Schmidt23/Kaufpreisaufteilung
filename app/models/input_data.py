from pydantic import BaseModel

from app.models.gebaeude import Gebaeude
from app.models.grundstueck import Grundstueck
from app.models.kaufvertrag import Kaufvertrag


class InputData(BaseModel):

    # Stammdaten
    kaufvertrag: Kaufvertrag
    grundstueck: Grundstueck
    gebaeude: Gebaeude

    # Gebäudedaten
    wohnflaeche: float | None = None
    nhk_code: str
    standardstufe: int
    bruttogrundflaeche: float

    # Modernisierung
    dachmodernisierung: str | None = None
    fenstermodernisierung: str | None = None
    leitungsmodernisierung: str | None = None
    heizungsmodernisierung: str | None = None
    waermedaemmung: str | None = None
    baedermodernisierung: str | None = None
    innenausbau: str | None = None
    grundriss: str | None = None

    # Bewertungsparameter
    regionalfaktor: float = 1.0
    sachwertfaktor: float = 1.0

    # Zwischenergebnisse
    gesamtnutzungsdauer: int | None = None
    modernisierungspunkte: int | None = None
    fiktives_baujahr: int | None = None
    restnutzungsdauer: int | None = None

    garagenwert: float = 0.0
    normalherstellungskosten: float | None = None
    alterswertminderung: float | None = None
    gebaeudesachwert: float | None = None
    marktangepasster_sachwert: float | None = None
    bodenwert: float | None = None
    vorlaeufiger_sachwert: float | None = None

    # Endergebnis
    bodenanteil: float | None = None
    gebaeudeanteil: float | None = None
    bodenanteil_prozent: float | None = None
    gebaeudeanteil_prozent: float | None = None