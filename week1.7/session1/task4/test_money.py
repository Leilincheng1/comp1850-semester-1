# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.7, Session 1: Task 4 - unit tests for methods in Money
#
# import pytest
#
# from money import Money
#
# def test_invalid_type_pound():
#     with pytest.raises(TypeError) as excinfo:
#         Money(1.2, 99)
#     assert str(excinfo.value) == "pounds must be an integer"
#
#
# def test_invalid_value_pound():
#     with pytest.raises(ValueError) as excinfo:
#         Money(-1, 0)
#     assert str(excinfo.value) == "pounds must be >= 0"
#
#
# def test_add_invalid_type():
#     m1 = Money(5, 0)
#     with pytest.raises(TypeError) as excinfo:
#         m1 + 42
#     assert str(excinfo.value) == "other object must be a Money"
#
#
# def test_invalid_type_pence():
    # complete the test implementation for 
    # invalid type for pence
#     
#
# def test_invalid_value_pence():
    # complete the test implementation for 
    # invalid value for pence
#     
#
# def test_valid_add():
    # complete the test implementation for
    # valid add between money objects
    # Hint: you can compare using the __str()__ (
    # e.g., str(m1 + m2) == "£2.04"
#     
# ============================================================================
# Completed solution
# ============================================================================
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
