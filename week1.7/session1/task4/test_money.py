"""Tests for Money constructor validation and addition."""
import pytest
from money import Money


def test_invalid_type_pound():
    with pytest.raises(TypeError, match="pounds must be an integer"):
        Money(1.2, 99)


def test_invalid_value_pound():
    with pytest.raises(ValueError, match="pounds must be >= 0"):
        Money(-1, 0)


def test_add_invalid_type():
    with pytest.raises(TypeError, match="other object must be a Money"):
        Money(5, 0) + 42


def test_invalid_type_pence():
    with pytest.raises(TypeError, match="pence must be an integer"):
        Money(1, "50")


def test_invalid_value_pence():
    with pytest.raises(ValueError, match="pence must be in range 0-99"):
        Money(1, -1)
    with pytest.raises(ValueError, match="pence must be in range 0-99"):
        Money(1, 100)


def test_valid_add():
    assert str(Money(1, 50) + Money(0, 54)) == "£2.04"
    assert str(Money(0, 0) + Money(0, 0)) == "£0.00"
    assert str(Money(5, 99) + Money(2, 1)) == "£8.00"
