"""Unit tests for summing empty, singleton and multi-item integer lists."""
from process_data import process_data


def test_empty_list():
    assert process_data([]) is None


def test_one_int_list():
    assert process_data([0]) == 0
    assert process_data([7]) == 7
    assert process_data([-4]) == -4


def test_multiple_int_list():
    assert process_data([1, 2, 3]) == 6
    assert process_data([-2, -3]) == -5
    assert process_data([5, -5, 0]) == 0
