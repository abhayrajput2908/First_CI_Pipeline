
from codes.rotate_list_27 import rotate_list


def test_normal_rotation():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_rotation_by_one():
    assert rotate_list([1, 2, 3, 4], 1) == [4, 1, 2, 3]


def test_rotation_by_zero():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]


def test_rotation_greater_than_length():
    assert rotate_list([1, 2, 3], 5) == [2, 3, 1]


def test_empty_list():
    assert rotate_list([], 2) == []


def test_single_element():
    assert rotate_list([10], 3) == [10]


def test_negative_rotation():
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]
