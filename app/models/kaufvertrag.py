from pydantic import BaseModel
from datetime import date

class Kaufvertrag(BaseModel):
    kaufpreis: float
    datum: date | None = None