# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 4, Session 1: 
#
# You are given an incomplete function isBond with a docstring. Your task
# is to complete the function based on the details in the docstring.
#
#
# def isBond(intList):
#     """
#     This function accepts a list of integers and returns True if the
#     sequence 0, 0, 7 appears in the list, in that order. Return False
#     otherwise. The numbers do not need to be consecutive, but must appear
#     in the specified order.
#     """
#
    # pass is a Python keyword used as a placeholder for future code,
    # meaning you need to delete pass to write your code.
    # Nothing happens when pass is executed.
#
#     pass     # delete pass to write your code
#
# Check if the following lines of code produce the correct output
# print(isBond([1, 2, 4, 0, 0, 7, 5]))   # True
# print(isBond([1, 0, 2, 4, 0, 5, 7]))   # True
# print(isBond([1, 7, 2, 0, 4, 5, 0]))   # False
# ============================================================================
# Completed solution
# ============================================================================
"""Detect a subsequence of 0, 0, 7 in a list of integers."""


def isBond(intList):
    """Return True if 0, 0, 7 appear in order, not necessarily consecutively."""
    expected = (0, 0, 7)
    next_index = 0
    for value in intList:
        if value == expected[next_index]:
            next_index += 1
            if next_index == len(expected):
                return True
    return False


if __name__ == "__main__":
    print(isBond([1, 2, 4, 0, 0, 7, 5]))
    print(isBond([1, 0, 2, 4, 0, 5, 7]))
    print(isBond([1, 7, 2, 0, 4, 5, 0]))
