from dataclasses import dataclass


@dataclass(frozen=True)
class FiktivesBaujahrParameter:
    modernisierungspunkte: int
    a: float
    b: float
    c: float

FIKTIVE_BAUJAHR_PARAMETER = [

    FiktivesBaujahrParameter(
        modernisierungspunkte=1,
        a=0.012500,
        b=2.625000,
        c=152.5000,
    ),

    FiktivesBaujahrParameter(
        modernisierungspunkte=2,
        a=0.010767,
        b=2.275667,
        c=138.7767,
    ),

    FiktivesBaujahrParameter(
        modernisierungspunkte=3,
        a=0.009033,
        b=1.926333,
        c=125.0533,
    ),

    FiktivesBaujahrParameter(
        modernisierungspunkte=4,
        a=0.007300,
        b=1.577000,
        c=111.3300,
    ),

    FiktivesBaujahrParameter(
        modernisierungspunkte=5,
        a=0.006725,
        b=1.457750,
        c=108.4975,
    ),

    FiktivesBaujahrParameter(
        modernisierungspunkte=6,
        a=0.006150,
        b=1.338500,
        c=105.6650,
    ),

    FiktivesBaujahrParameter(
        modernisierungspunkte=7,
        a=0.005575,
        b=1.219250,
        c=102.8325,
    ),

    FiktivesBaujahrParameter(
        modernisierungspunkte=8,
        a=0.005000,
        b=1.100000,
        c=100.0000,
    ),

    FiktivesBaujahrParameter(
        modernisierungspunkte=9,
        a=0.004660,
        b=1.027000,
        c=99.0560,
    ),

    FiktivesBaujahrParameter(
        modernisierungspunkte=10,
        a=0.004320,
        b=0.954000,
        c=98.1120,
    ),

    FiktivesBaujahrParameter(
        modernisierungspunkte=11,
        a=0.003980,
        b=0.881000,
        c=97.1680,
    ),

    FiktivesBaujahrParameter(
        modernisierungspunkte=12,
        a=0.003640,
        b=0.808000,
        c=96.2240,
    ),

    FiktivesBaujahrParameter(
        modernisierungspunkte=13,
        a=0.003300,
        b=0.735000,
        c=95.2800,
    ),

    FiktivesBaujahrParameter(
        modernisierungspunkte=14,
        a=0.003040,
        b=0.676000,
        c=95.0640,
    ),

    FiktivesBaujahrParameter(
        modernisierungspunkte=15,
        a=0.002780,
        b=0.617000,
        c=94.8480,
    ),

    FiktivesBaujahrParameter(
        modernisierungspunkte=16,
        a=0.002520,
        b=0.558000,
        c=94.6320,
    ),

    FiktivesBaujahrParameter(
        modernisierungspunkte=17,
        a=0.002260,
        b=0.499000,
        c=94.4160,
    ),

    FiktivesBaujahrParameter(
        modernisierungspunkte=18,
        a=0.002000,
        b=0.440000,
        c=94.2000,
    ),
]

def finde_parameter(
    modernisierungspunkte: float,
) -> FiktivesBaujahrParameter:

    punkte = round(modernisierungspunkte)

    if punkte < 1:
        punkte = 1

    if punkte > 18:
        punkte = 18

    for parameter in FIKTIVE_BAUJAHR_PARAMETER:
        if (
            parameter.modernisierungspunkte
            == punkte
        ):
            return parameter

    raise ValueError(
        f"Kein Parameter für {punkte} Punkte vorhanden."
    )
