# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 4, Session 2: Task 4
#
# Given incomplete recursive function digits_sum with a docstring,
# your task is to complete the function based on the description
#
#
# def digits_sum(number):
#     """
#     This recursive function calculates the sum of digits of a given positive
#     integer. For example, sum of digits for 987 = 9 + 8 + 7 = 24.
#     For simplisity, ignore the case when number is not an integer or
#     not a positive integer.
#
#     Args:
#         number (int): The input is a positive integer.
#
#     Returns:
#         int: The sum of the digits of the input integer.
#     """
    # complete your code here
    # base case
#
    # recursive case
#
#
# check if correct output is produced
# print(digits_sum(987))  # Output: 24
# print(digits_sum(12345))  # Output: 15
#
#
# Once completed, your next task is to write an equivalent function that uses loops.
# ============================================================================
# Completed solution
# ============================================================================
"""Sum the digits of a nonnegative integer recursively and iteratively."""


def digits_sum(number):
    """Return the sum of decimal digits via recursion."""
    if number < 10:
        return number
    return number % 10 + digits_sum(number // 10)


def digits_sum_loop(number):
    """Return digit sum using a while loop."""
    total = 0
    while number:
        total += number % 10
        number //= 10
    return total


if __name__ == "__main__":
    for value in (987, 12345):
        print(digits_sum(value))
        assert digits_sum(value) == digits_sum_loop(value)
