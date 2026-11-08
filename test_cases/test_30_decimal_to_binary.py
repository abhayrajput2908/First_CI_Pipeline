
import pytest

from codes.decimal_to_binary_30 import decimal_to_binary


def test_decimal_to_binary_10():
    assert decimal_to_binary(10) == "1010"


def test_decimal_to_binary_5():
    assert decimal_to_binary(5) == "101"


def test_decimal_to_binary_0():
    assert decimal_to_binary(0) == "0"


def test_decimal_to_binary_1():
    assert decimal_to_binary(1) == "1"


def test_decimal_to_binary_255():
    assert decimal_to_binary(255) == "11111111"


def test_negative_number():
    with pytest.raises(ValueError):
        decimal_to_binary(-5)
