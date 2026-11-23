import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-2, 3) == 1


def test_subtract(calc):
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(4, 10) == -6


def test_multiply(calc):
    assert calc.multiply(3, 5) == 15
    assert calc.multiply(3, 0) == 0


def test_divide(calc):
    assert calc.divide(10, 2) == 5


def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(5, 0)
