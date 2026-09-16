import json
from pathlib import Path
import pytest

from app.calculator.engine import CalculationEngine
from app.models.input_data import InputData

REFERENCE_CASES = sorted(
    (
        Path(__file__).parent
        / "reference_cases"
    ).glob("*.json")
)


@pytest.mark.parametrize(
    "path",
    REFERENCE_CASES,
)
def test_reference_case(path):

    with open(path, encoding="utf-8") as f:
        case = json.load(f)

    data = InputData(**case["input"])

    result = CalculationEngine().calculate(data)

    expected = case["expected"]

    for key, expected_value in expected.items():

        actual_value = getattr(result, key)

        if isinstance(expected_value, float):
            assert actual_value == pytest.approx(expected_value)
        else:
            assert actual_value == expected_value

def test_reference_case_kaufpreisaufteilung_ergibt_kaufpreis():

    for path in REFERENCE_CASES:

        with open(path, encoding="utf-8") as f:
            case = json.load(f)

        data = InputData(**case["input"])

        result = CalculationEngine().calculate(data)

        assert (
            result.bodenanteil
            + result.gebaeudeanteil
            == pytest.approx(
                data.kaufvertrag.kaufpreis
            )
        )

def test_reference_case_anteile_prozent_ergibt_100():

    for path in REFERENCE_CASES:

        with open(path, encoding="utf-8") as f:
            case = json.load(f)

        data = InputData(**case["input"])

        result = CalculationEngine().calculate(data)

        assert (
            result.bodenanteil_prozent
            + result.gebaeudeanteil_prozent
            == pytest.approx(100.0)
        )

def test_reference_case_folgewerte():

    for path in REFERENCE_CASES:

        with open(path, encoding="utf-8") as f:
            case = json.load(f)

        data = InputData(**case["input"])

        result = CalculationEngine().calculate(data)

        assert result.bodenwert == pytest.approx(
            case["expected"]["bodenwert"]
        )

        assert result.vorlaeufiger_sachwert == pytest.approx(
            case["expected"]["vorlaeufiger_sachwert"]
        )

        assert result.marktangepasster_sachwert == pytest.approx(
            case["expected"]["marktangepasster_sachwert"]
        )

        assert result.gebaeudeanteil == pytest.approx(
            case["expected"]["gebaeudeanteil"]
        )

        assert result.bodenanteil == pytest.approx(
            case["expected"]["bodenanteil"]
        )

        assert result.gebaeudeanteil_prozent == pytest.approx(
            case["expected"]["gebaeudeanteil_prozent"]
        )

        assert result.bodenanteil_prozent == pytest.approx(
            case["expected"]["bodenanteil_prozent"]
        )