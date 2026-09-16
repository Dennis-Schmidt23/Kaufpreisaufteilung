from pydantic import BaseModel


class Grundstueck(BaseModel):
    flaeche_1: float
    bodenrichtwert_1: float

    flaeche_2: float = 0.0
    bodenrichtwert_2: float = 0.0

    miteigentumsanteil_zaehler: float | None = None
    miteigentumsanteil_nenner: float | None = None