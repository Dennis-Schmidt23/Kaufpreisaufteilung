from enum import Enum


class Section(str, Enum):
    ALLGEMEIN = "Allgemeine Angaben"
    GRUNDSTUECK = "Grundstück"
    GEBAEUDE = "Gebäude"
    VERGLEICHSWERT = "Vergleichswertverfahren"
    ERTRAGSWERT = "Ertragswertverfahren"
    SACHWERT = "Sachwertverfahren"