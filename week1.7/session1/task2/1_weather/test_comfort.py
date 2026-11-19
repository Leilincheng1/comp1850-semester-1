"""Unit tests for all comfort levels, including thresholds."""
from weather import comfort_level


def test_cold():
    assert comfort_level(-5.0) == "COLD"
    assert comfort_level(15.0) == "COLD"


def test_hot():
    assert comfort_level(25.1) == "HOT"
    assert comfort_level(40.0) == "HOT"


def test_ok():
    assert comfort_level(15.1) == "OK"
    assert comfort_level(20.0) == "OK"
    assert comfort_level(25.0) == "OK"
