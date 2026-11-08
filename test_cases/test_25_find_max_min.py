
from codes.find_max_min_25 import find_max_min


def test_positive_numbers():
    assert find_max_min([10, 20, 5, 30]) == (30, 5)


def test_negative_numbers():
    assert find_max_min([-10, -20, -5]) == (-5, -20)


def test_mixed_numbers():
    assert find_max_min([-10, 20, 0, 30, -5]) == (30, -10)


def test_single_number():
    assert find_max_min([15]) == (15, 15)


def test_empty_list():
    assert find_max_min([]) == (None, None)

