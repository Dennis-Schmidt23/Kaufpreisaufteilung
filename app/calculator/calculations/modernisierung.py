from enum import Enum


class Modernisierung(str, Enum):
    JA = "ja"
    TEILWEISE = "teilweise"
    NEIN = "nein"


def punkte(status: Modernisierung, max_punkte: int) -> float:
    if status == Modernisierung.JA:
        return float(max_punkte)

    if status == Modernisierung.TEILWEISE:
        return max_punkte / 2

    return 0.0


def calculate_modernisierungspunkte(
    data: InputData,
) -> float:
    return (
        punkte(data.dachmodernisierung, 4)
        + punkte(data.fenstermodernisierung, 2)
        + punkte(data.leitungsmodernisierung, 2)
        + punkte(data.heizungsmodernisierung, 2)
        + punkte(data.waermedaemmung, 4)
        + punkte(data.baedermodernisierung, 2)
        + punkte(data.innenausbau, 2)
        + punkte(data.grundriss, 2)
    )
