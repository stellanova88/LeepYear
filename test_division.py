import pytest
from divide_number import divide


def test_divide_number_with_0():
    with pytest.raises(ZeroDivisionError):
        divide(2, 0)
        divide(400, 0)
        divide(5, 0)


def test_divide_by_one_gives_the_same_number_trying_to_divide():
    assert divide(2, 1) == 2
    assert divide(4, 1) == 4
    assert divide(40, 1) == 40


def test_divide_by_2_give_half_the_number():
    assert divide(2, 2) == 1
    assert divide(10, 2) == 5
    assert divide(6, 2) == 3


def test_any_number_divided_by_the_same_number_gives_1():
    assert divide(1, 1) == 1
    assert divide(3, 3) == 1
    assert divide(5, 5) == 1
    assert divide(2000, 2000) == 1


def test_divide_numbers_in_the_correct_order():
    assert divide(2, 10) < 1
    assert divide(30, 31) < 1
    assert divide(1, 2) < 1
    assert divide(2, 5) < 1


def test_negative_number_divided_with_negative_gives_positive_number():
    assert divide(-8, -2) == 4
    assert divide(-2, -1) == 2
    assert divide(-3, -3) == 1