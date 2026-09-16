from dataclasses import dataclass, field
from typing import Optional
from typing import Literal
from app.calculator.data.nhk import nhk_form_options


@dataclass(frozen=True)
class FormField:
    name: str
    label: str

    field_type: Literal[
        "text",
        "number",
        "date",
        "select",
        "radio",
        "checkbox"
    ]

    required: bool = True

    placeholder: str = ""
    help_text: str = ""

    unit: str = ""

    min_value: float | None = None
    max_value: float | None = None

    step: str = "0.01"

    options: list[dict[str, str]] | None = None

@dataclass(frozen=True)
class FormSection:
    title: str
    description: str = ""
    fields: list[FormField] = field(default_factory=list)

FORM_SECTIONS = [
    FormSection(
        title="Kaufvertrag",
        description="Angaben aus dem notariellen Kaufvertrag.",
        fields=[
            FormField(
                name="kaufpreis",
                label="Kaufpreis (€)",
                field_type="number",
                required=True,
                placeholder="500000",
                help_text="Gesamtkaufpreis laut Kaufvertrag.",
                min_value=0,
            ),
            FormField(
                name="datum",
                label="Kaufvertragsdatum",
                field_type="date",
                required=True,
                help_text="Datum des notariellen Kaufvertrags.",
            ),
        ],
    ),
    FormSection(
        title="Grund und Boden",
        description="Angaben zum Grundstück.",
        fields=[
            FormField(
                name="grundstuecksflaeche",
                label="Grundstücksfläche (m²)",
                field_type="number",
                required=True,
                placeholder="600",
                help_text="Fläche des Grundstücks.",
                min_value=0,
            ),
            FormField(
                name="bodenrichtwert",
                label="Bodenrichtwert (€/m²)",
                field_type="number",
                required=True,
                placeholder="350",
                help_text="Bodenrichtwert laut Bodenrichtwertkarte.",
                min_value=0,
            ),
            FormField(
                name="grundstuecksflaeche_2",
                label="Weitere Grundstücksfläche (m²)",
                field_type="number",
                required=False,
                placeholder="0",
                min_value=0,
            ),
            FormField(
                name="bodenrichtwert_2",
                label="Weiterer Bodenrichtwert (€/m²)",
                field_type="number",
                required=False,
                placeholder="0",
                min_value=0,
            ),
            FormField(
                name="miteigentumsanteil_zaehler",
                label="Miteigentumsanteil – Zähler",
                field_type="number",
                required=False,
                placeholder="1",
                help_text="Zähler des Miteigentumsanteils, z. B. 1 bei 1/2.",
                min_value=1,
                step="1",
            ),
            FormField(
                name="miteigentumsanteil_nenner",
                label="Miteigentumsanteil – Nenner",
                field_type="number",
                required=False,
                placeholder="2",
                help_text="Nenner des Miteigentumsanteils, z. B. 2 bei 1/2.",
                min_value=1,
                step="1",
            ),
        ],
    ),
    FormSection(
        title="Gebäude",
        description="Angaben zum Gebäude.",
        fields=[
            FormField(
                name="baujahr",
                label="Baujahr",
                field_type="number",
                required=True,
                min_value=1800,
                max_value=2100,
                step="1",
            ),
            FormField(
                name="wohnflaeche",
                label="Wohnfläche (m²)",
                field_type="number",
                min_value=0,
                step="0.1",
            ),
            FormField(
                name="nhk_code",
                label="Gebäudeart / NHK-Typ",
                field_type="select",
                required=True,
                options=nhk_form_options(),
                help_text="Gebäudeart gemäß BMF-Arbeitshilfe.",

            ),
            FormField(
                name="standardstufe",
                label="Standardstufe",
                field_type="select",
                required=True,
                options=[
                    {"value": "1", "label": "1 – einfach"},
                    {"value": "2", "label": "2 – einfach bis mittel"},
                    {"value": "3", "label": "3 – mittel"},
                    {"value": "4", "label": "4 – mittel bis gehoben"},
                    {"value": "5", "label": "5 – gehoben"},
                ]
            ),
            FormField(
                name="bruttogrundflaeche",
                label="Bruttogrundfläche (m²)",
                field_type="number",
                required=True,
                min_value=0,
            ),
        ],
    ),
    FormSection(
        title="Stellplätze",
        description="Angaben zu Stellplätzen.",
        fields=[
            FormField(
                name="garagenstellplaetze",
                label="Garagenstellplätze",
                field_type="number",
                placeholder="0",
                help_text="Anzahl der Garagenstellplätze.",
                min_value=0,
                step="1",
            ),
            FormField(
                name="tiefgaragenstellplaetze",
                label="Tiefgaragenstellplätze",
                field_type="number",
                placeholder="0",
                help_text="Anzahl der Tiefgaragenstellplätze.",
                min_value=0,
                step="1",
            ),
        ],
    ),
    FormSection(
        title="Bewertungsparameter",
        description="Regionale Bewertungsparameter.",
        fields=[
            FormField(
                name="regionalfaktor",
                label="Regionalfaktor",
                field_type="number",
                required=False,
                placeholder="1,00",
                help_text="Regionalfaktor gemäß BMF-Arbeitshilfe.",
                min_value=0,
                step="0.01",
            ),
            FormField(
                name="sachwertfaktor",
                label="Sachwertfaktor",
                field_type="number",
                required=False,
                placeholder="1,00",
                help_text="Sachwertfaktor des zuständigen Gutachterausschusses.",
                min_value=0,
                step="0.0001",
            ),
        ],
    ),
    FormSection(
        title="Modernisierung",
        description="Modernisierungsmaßnahmen nach der BMF-Arbeitshilfe.",
        fields=[
            FormField(
                name="dachmodernisierung",
                label="Dach",
                field_type="select",
                options=[
                    {"value": "Keine", "label": "Keine"},
                    {"value": "Teilweise", "label": "Teilweise"},
                    {"value": "Umfassend", "label": "Umfassend"},
                ],
            ),
            FormField(
                name="fenstermodernisierung",
                label="Fenster",
                field_type="select",
                options=[
                    {"value": "Keine", "label": "Keine"},
                    {"value": "Teilweise", "label": "Teilweise"},
                    {"value": "Umfassend", "label": "Umfassend"},
                ],
            ),
            FormField(
                name="leitungsmodernisierung",
                label="Leitungen",
                field_type="select",
                options=[
                    {"value": "Keine", "label": "Keine"},
                    {"value": "Teilweise", "label": "Teilweise"},
                    {"value": "Umfassend", "label": "Umfassend"},
                ],
            ),
            FormField(
                name="heizungsmodernisierung",
                label="Heizung",
                field_type="select",
                options=[
                    {"value": "Keine", "label": "Keine"},
                    {"value": "Teilweise", "label": "Teilweise"},
                    {"value": "Umfassend", "label": "Umfassend"},
                ],
            ),
            FormField(
                name="waermedaemmung",
                label="Wärmedämmung",
                field_type="select",
                options=[
                    {"value": "Keine", "label": "Keine"},
                    {"value": "Teilweise", "label": "Teilweise"},
                    {"value": "Umfassend", "label": "Umfassend"},
                ],
            ),
            FormField(
                name="innenausbau",
                label="Innenausbau",
                field_type="select",
                options=[
                    {"value": "Keine", "label": "Keine"},
                    {"value": "Teilweise", "label": "Teilweise"},
                    {"value": "Umfassend", "label": "Umfassend"},
                ],
            ),
            FormField(
                name="grundriss",
                label="Grundriss",
                field_type="select",
                options=[
                    {"value": "Keine", "label": "Keine"},
                    {"value": "Teilweise", "label": "Teilweise"},
                    {"value": "Umfassend", "label": "Umfassend"},
                ],
            ),
            FormField(
                name="baedermodernisierung",
                label="Bäder",
                field_type="select",
                options=[
                    {"value": "Keine", "label": "Keine"},
                    {"value": "Teilweise", "label": "Teilweise"},
                    {"value": "Umfassend", "label": "Umfassend"},
                ],
            ),
        ],
    ),
]
