# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 4, Session 2: Task 4
#
# Given an incomplete recursive function power to calculate x raised to
# the power of n, your task is to complete the function.
#
#
# def power(x, n):
    # complete your code here
    # base case
#
    # recursive case
#
#
# Once completed, make at least two function calls to test the power function
# ============================================================================
# Completed solution
# ============================================================================
"""Raise a number to an integer power recursively."""


def power(x, n):
    """Return x**n for an integer exponent n."""
    if not isinstance(n, int):
        raise TypeError("Exponent must be an integer")
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    return x * power(x, n - 1)


if __name__ == "__main__":
    print(power(2, 5))
    print(power(3, 3))
    assert power(2, 5) == 32
    assert power(3, 3) == 27
