from app.calculator.data.baupreisindex import (
    finde_baupreisindex,
)
import pytest
from datetime import date
from app.calculator.data.baupreisindex import (
    finde_baupreisindex,
)


def test_unbekanntes_jahr():

    with pytest.raises(ValueError):
        finde_baupreisindex(1990)


def test_baupreisindex_2026():

    index = finde_baupreisindex(2026)

    assert index.index == 189.1