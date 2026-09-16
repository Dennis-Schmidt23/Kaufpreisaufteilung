from dataclasses import dataclass


@dataclass(frozen=True)
class Baupreisindex:
    jahr: int
    index: float

BAUPREISINDIZES = {
    2026: Baupreisindex(2026, 189.1),
    2025: Baupreisindex(2025, 189.1),
    2024: Baupreisindex(2024, 183.3),
    2023: Baupreisindex(2023, 177.9),
    2022: Baupreisindex(2022, 164.0),
    2021: Baupreisindex(2021, 141.0),
    2020: Baupreisindex(2020, 129.2),
    2019: Baupreisindex(2019, 127.2),
    2018: Baupreisindex(2018, 122.0),
    2017: Baupreisindex(2017, 116.8),
    2016: Baupreisindex(2016, 113.4),
    2015: Baupreisindex(2015, 111.1),
    2014: Baupreisindex(2014, 109.4),
    2013: Baupreisindex(2013, 107.5),
    2012: Baupreisindex(2012, 105.4),
    2011: Baupreisindex(2011, 102.8),
    2010: Baupreisindex(2010, 100.0),
}

def finde_baupreisindex(jahr: int) -> Baupreisindex:
    try:
        return BAUPREISINDIZES[jahr]
    except KeyError:
        raise ValueError(
            f"Kein Baupreisindex für Jahr {jahr} vorhanden."
        )