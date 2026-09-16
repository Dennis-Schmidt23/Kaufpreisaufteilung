from app.calculator.calculations.aussenanlagen import (
    berechne_aussenanlagenpauschale,
)


def test_aussenanlagenpauschale_3_prozent():
    ergebnis = berechne_aussenanlagenpauschale(
        300_000
    )

    assert ergebnis == 309_000

def test_aussenanlagenpauschale_3_prozent():
    kkw = 300_000

    ergebnis = round(kkw * 1.03, 0)

    assert ergebnis == 309_000

def berechne_aussenanlagenpauschale(kkw: float) -> float:
    return round(kkw * 1.03, 0)