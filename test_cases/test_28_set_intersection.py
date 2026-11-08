
from codes.set_intersection_28 import set_intersection


def test_normal_intersection():
    assert set_intersection([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]


def test_no_common_elements():
    assert set_intersection([1, 2], [3, 4]) == []


def test_identical_lists():
    assert set_intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3]


def test_duplicate_elements():
    assert set_intersection([1, 2, 2, 3], [2, 2, 3, 3]) == [2, 3]


def test_empty_lists():
    assert set_intersection([], []) == []


def test_negative_numbers():
    assert set_intersection([-1, -2, 3], [-2, 3, 4]) == [-2, 3]
