from dataclasses import asdict
import json
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.calculator.engine import CalculationEngine
from app.models.input_data import InputData


REFERENCE_CASE_DIR = Path(
    "tests/reference_cases"
)


def update_reference_case(path: Path) -> None:
    """Aktualisiert einen einzelnen Referenzfall."""

    with path.open(
        encoding="utf-8"
    ) as f:
        case = json.load(f)

    data = InputData(**case["input"])

    result = (
        CalculationEngine()
        .calculate(data)
    )

    new_expected = asdict(result)

    if case["expected"] != new_expected:
        case["expected"] = new_expected

        with path.open(
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                case,
                f,
                indent=4,
                ensure_ascii=False,
            )

        print(f"✓ {path.name}")
    else:
        print(f"• {path.name} unverändert")

def main() -> None:
    print("Aktualisiere Referenzfälle...\n")

    paths = sorted(
        REFERENCE_CASE_DIR.glob("*.json")
    )

    if not paths:
        print(
            "Keine Referenzfälle gefunden."
        )
        return

    for path in paths:
        update_reference_case(path)

    print(
        f"\n{len(paths)} Referenzfälle aktualisiert."
    )


if __name__ == "__main__":
    main()
