from dataclasses import dataclass
from enum import Enum

@dataclass
class CalculationResult:

    bodenwert: float = 0.0

    normalherstellungskosten: float = 0.0

    gebaeudesachwert: float = 0.0

    modernisierungspunkte: float = 0.0

    fiktives_baujahr: int | None = None

    restnutzungsdauer: int | None = None

    alterswertminderung: float = 0.0

    garagenwert: float = 0.0

    vorlaeufiger_sachwert: float = 0.0

    marktangepasster_sachwert: float = 0.0

    sachwertfaktor: float = 1.0

    bodenanteil: float = 0.0
    gebaeudeanteil: float = 0.0

    bodenanteil_prozent: float = 0.0
    gebaeudeanteil_prozent: float = 0.0

    def to_dict(self) -> dict:

        result = {}

        for key, value in self.__dict__.items():

            if isinstance(value, Enum):
                result[key] = value.value

            else:
                result[key] = value

        return result