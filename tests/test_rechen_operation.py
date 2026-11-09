import pytest

from aufgaben_package.rechen_operation import (
    erhoehe_um_zwei,
    multipliziere_mit_drei,
    subtrahiere_zehn,
    teile_durch_vier,
)


@pytest.mark.parametrize(
    ("zahl", "ergebnis"),
    [(0, 2), (5, 7), (-3, -1)],
)
def test_erhoehe_um_zwei(zahl, ergebnis):
    assert erhoehe_um_zwei(zahl) == ergebnis


@pytest.mark.parametrize(
    ("zahl", "ergebnis"),
    [(0, 0), (4, 12), (-3, -9)],
)
def test_multipliziere_mit_drei(zahl, ergebnis):
    assert multipliziere_mit_drei(zahl) == ergebnis


@pytest.mark.parametrize(
    ("zahl", "ergebnis"),
    [(0, -10), (10, 0), (-5, -15)],
)
def test_subtrahiere_zehn(zahl, ergebnis):
    assert subtrahiere_zehn(zahl) == ergebnis


@pytest.mark.parametrize(
    ("zahl", "ergebnis"),
    [(0, 0.0), (8, 2.0), (-12, -3.0)],
)
def test_teile_durch_vier(zahl, ergebnis):
    assert teile_durch_vier(zahl) == ergebnis


@pytest.mark.parametrize("zahl", [1, 2, -3])
def test_teile_durch_vier_raises_for_non_divisible_number(zahl):
    with pytest.raises(ValueError, match="Zahl muss durch 4 teilbar sein"):
        teile_durch_vier(zahl)