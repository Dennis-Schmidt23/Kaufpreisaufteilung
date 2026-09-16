from dataclasses import dataclass
from enum import Enum


class Section(str, Enum):
    ALLGEMEIN = "Allgemeine Angaben"
    VERGLEICHSWERT = "Vergleichswertverfahren"
    ERTRAGSWERT = "Ertragswertverfahren"
    SACHWERT = "Sachwertverfahren"


class FieldType(str, Enum):
    TEXT = "text"
    NUMBER = "number"
    DATE = "date"
    SELECT = "select"
    CHECKBOX = "checkbox"


@dataclass(frozen=True)
class FieldDefinition:
    nummer: int
    section: Section
    name: str
    label: str
    field_type: FieldType
    required: bool = True
    unit: str = ""
    help_text: str = ""

FIELD_CATALOG = [

    FieldDefinition(
        nummer=1,
        section=Section.ALLGEMEIN,
        name="lage",
        label="Lage des Grundstücks",
        field_type=FieldType.TEXT,
    ),

    FieldDefinition(
        nummer=2,
        section=Section.ALLGEMEIN,
        name="grundstuecksart",
        label="Grundstücksart",
        field_type=FieldType.SELECT,
    ),

    FieldDefinition(
        nummer=3,
        section=Section.ALLGEMEIN,
        name="kaufvertragsdatum",
        label="Datum des Kaufvertrags",
        field_type=FieldType.DATE,
    ),

    FieldDefinition(
        nummer=5,
        section=Section.ALLGEMEIN,
        name="baujahr",
        label="Ursprüngliches Baujahr",
        field_type=FieldType.NUMBER,
    ),

    FieldDefinition(
        nummer=7,
        section=Section.ALLGEMEIN,
        name="garagen",
        label="Anzahl Garagenstellplätze",
        field_type=FieldType.NUMBER,
        required=False,
    ),

    FieldDefinition(
        nummer=9,
        section=Section.ALLGEMEIN,
        name="miteigentumsanteil_zaehler",
        label="Miteigentumsanteil – Zähler",
        field_type=FieldType.NUMBER,
        required=False,
    ),

    FieldDefinition(
        nummer=11,
        section=Section.ALLGEMEIN,
        name="flaeche_1",
        label="Fläche 1 – Grundstücksgröße",
        field_type=FieldType.NUMBER,
        unit="m²",
    ),

    FieldDefinition(
        nummer=13,
        section=Section.ALLGEMEIN,
        name="flaeche_2",
        label="Fläche 2 – Grundstücksgröße",
        field_type=FieldType.NUMBER,
        required=False,
        unit="m²",
    ),
]