from app.calculator.calculations.bodenwert import calculate_bodenwert
from app.models.input_data import InputData
from app.calculator.result import CalculationResult
from app.calculator.calculations.gebaeudesachwert import (
    calculate_gebaeudesachwert,
)
from app.calculator.calculations.modernisierung import (
    calculate_modernisierungspunkte,
)
from app.calculator.calculations.fiktives_baujahr import (
    calculate_fiktives_baujahr,
)
from app.calculator.calculations.normalherstellungskosten import (
    calculate_normalherstellungskosten,
)
from app.calculator.calculations.restnutzungsdauer import (
    calculate_restnutzungsdauer,
)
from app.calculator.calculations.alterswertminderung import (
    calculate_alterswertminderung,
)
from app.calculator.calculations.vorlaeufiger_sachwert import (
    calculate_vorlaeufiger_sachwert,
)
from app.calculator.calculations.bodenanteil import (
    calculate_bodenanteil,
)
from app.calculator.calculations.gebaeudeanteil import (
    calculate_gebaeudeanteil,
)
from app.calculator.calculations.anteile_prozent import (
    calculate_bodenanteil_prozent,
    calculate_gebaeudeanteil_prozent,
)
from app.calculator.calculations.marktangepasster_sachwert import (
    calculate_marktangepasster_sachwert,
)
from app.calculator.validation import validate
from app.calculator.calculations.garagenwert import (
    calculate_garagenwert,
)
from app.calculator.data.nhk import (
    finde_nhk_datensatz,
)
from app.calculator.data.baupreisindex import (
    finde_baupreisindex,
)

class CalculationEngine:

    def calculate(self, data: InputData):

        nhk = finde_nhk_datensatz(data.nhk_code)

        data.gesamtnutzungsdauer = (
            nhk.gesamtnutzungsdauer
        )
        validate(data)

        result = CalculationResult()


        baupreisindex = finde_baupreisindex(
            data.kaufvertrag.datum.year
        )

        result.bodenwert = calculate_bodenwert(data)
        data.bodenwert = result.bodenwert

        result.modernisierungspunkte = (
            calculate_modernisierungspunkte(data)
        )
        data.modernisierungspunkte = (
            result.modernisierungspunkte
        )

        result.normalherstellungskosten = (
            calculate_normalherstellungskosten(
                data,
                nhk,
                baupreisindex,
            )
        )
        data.normalherstellungskosten = (
            result.normalherstellungskosten
        )

        result.fiktives_baujahr = (
            calculate_fiktives_baujahr(data)
        )
        data.fiktives_baujahr = (
            result.fiktives_baujahr
        )

        result.restnutzungsdauer = (
            calculate_restnutzungsdauer(data)
        )
        data.restnutzungsdauer = (
            result.restnutzungsdauer
        )

        result.alterswertminderung = (
            calculate_alterswertminderung(data)
        )
        data.alterswertminderung = (
            result.alterswertminderung
        )

        result.garagenwert = calculate_garagenwert(data)
        data.garagenwert = result.garagenwert

        result.gebaeudesachwert = (
            calculate_gebaeudesachwert(data)
        )
        data.gebaeudesachwert = (
            result.gebaeudesachwert
        )

        # Sachwert
        result.vorlaeufiger_sachwert = (
            calculate_vorlaeufiger_sachwert(data)
        )
        data.vorlaeufiger_sachwert = (
            result.vorlaeufiger_sachwert
        )

        # Marktanpassung

        result.sachwertfaktor = data.sachwertfaktor
        data.sachwertfaktor = result.sachwertfaktor

        result.marktangepasster_sachwert = (
            calculate_marktangepasster_sachwert(data)
        )
        data.marktangepasster_sachwert = (
            result.marktangepasster_sachwert
        )

        result.gebaeudeanteil_prozent = (
            calculate_gebaeudeanteil_prozent(data)
        )
        data.gebaeudeanteil_prozent = (
            result.gebaeudeanteil_prozent
        )

        result.bodenanteil_prozent = (
            calculate_bodenanteil_prozent(data)
        )
        data.bodenanteil_prozent = (
            result.bodenanteil_prozent
        )

        # Kaufpreisaufteilung
        result.gebaeudeanteil = (
            calculate_gebaeudeanteil(data)
        )
        data.gebaeudeanteil = (
            result.gebaeudeanteil
        )

        result.bodenanteil = (
            calculate_bodenanteil(data)
        )
        data.bodenanteil = (
            result.bodenanteil
        )
        return result
