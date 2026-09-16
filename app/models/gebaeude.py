from pydantic import BaseModel

class Gebaeude(BaseModel):
    baujahr: int

    garagenstellplaetze: int = 0
    tiefgaragenstellplaetze: int = 0
