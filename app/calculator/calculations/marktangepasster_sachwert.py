

def calculate_marktangepasster_sachwert(data):

    if data.vorlaeufiger_sachwert is None:
        raise ValueError(
            "Vorlaeufiger Sachwert ist nicht gesetzt."
        )

    if data.sachwertfaktor is None:
        raise ValueError(
            "Sachwertfaktor ist nicht gesetzt."
        )

    return (
        round(data.sachwertfaktor, 4)
        * data.vorlaeufiger_sachwert
    )