from enum import Enum


class Gebaeudetyp(str, Enum):
    EINFAMILIENHAUS = "Einfamilienhaus"
    ZWEIFAMILIENHAUS = "Zweifamilienhaus"
    REIHENHAUS = "Reihenhaus"
    DOPPELHAUSHAELFTE = "Doppelhaushälfte"
    MEHRFAMILIENHAUS = "Mehrfamilienhaus"