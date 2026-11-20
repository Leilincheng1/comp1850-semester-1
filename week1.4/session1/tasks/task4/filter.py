"""Demonstrate a positive-number filtering function."""


def filter_positive_numbers(numbers):
    """Return all strictly positive values from a list of integers.

    Args:
        numbers (list of int): Values to filter.

    Returns:
        list of int: Positive numbers from the original list in their original order.
    """
    return [number for number in numbers if number > 0]
