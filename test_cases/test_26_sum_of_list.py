
from codes.sum_of_list_26 import sum_of_list


def test_positive_numbers():
    assert sum_of_list([1, 2, 3, 4, 5]) == 15


def test_negative_numbers():
    assert sum_of_list([-1, -2, -3]) == -6


def test_mixed_numbers():
    assert sum_of_list([10, -5, 20, -10]) == 15


def test_empty_list():
    assert sum_of_list([]) == 0


def test_single_number():
    assert sum_of_list([25]) == 25
