import pytest
from main import is_leap_year


def test_year_is_leap_year_when_dividing_by_400():
    assert is_leap_year(1600)
    assert is_leap_year(2000)
    assert is_leap_year(2400)


def test_year_is_leap_year_when_divisible_by_4_and_not_100():
    assert is_leap_year(1992)
    assert is_leap_year(1996)
    assert is_leap_year(2004)


def test_year_is_not_leap_year_when_divisible_by100_but_not_400():
    assert not is_leap_year(1700)
    assert not is_leap_year(1800)
    assert not is_leap_year(1900)


def test_year_is_not_leap_year_when_divisible_by_4():
    assert not is_leap_year(1701)
    assert not is_leap_year(3)
    assert not is_leap_year(2021)

