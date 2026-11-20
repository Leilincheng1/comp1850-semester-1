# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 4, Session 1: 
#
# Your are given the function filter_positive_numbers with a docstring.
# Can you identify the inconsistency between the docstring and the implementation?
#
# Your task is to update the docstring to reflect what the function does.
#
#
# def filter_positive_numbers(numbers):
#     """
#     Filters out positive numbers from the list, keeping only the negative ones.
#     The function returns a list of all the positive numbers in the input.
#
#     Args:
#         numbers (list of int): A list of integers.
#
#     Returns:
#         list of int: A list containing only the positive integers.
#     """
#     return [num for num in numbers if num > 0]
# ============================================================================
# Completed solution
# ============================================================================
"""Demonstrate a positive-number filtering function."""


def filter_positive_numbers(numbers):
    """Return all strictly positive values from a list of integers.

    Args:
        numbers (list of int): Values to filter.

    Returns:
        list of int: Positive numbers from the original list in their original order.
    """
    return [number for number in numbers if number > 0]
