# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# """
#     THIS IS NOT FOR BEGINNER, PLEASE IGNORE THIS TASK IF YOU ARE
#     NEW TO PROGRAMMING.
#
#     Write a recursive function moving_cummulative_sum() that calculate the
#     moving cummulative sum of integer values in a list and returns the
#     new list. For example, given a list [5,6,7,1,2,3], the resulting list
#     is [5,11,18,19,21,24].
#
#     This is an open-ended question in which you are free to determine
#     the number of parameters for the function, with the first argument is
#     for the list such as moving_cummulative_sum(x) with x being the
#     list to be operated on.
# """
# ============================================================================
# Completed solution
# ============================================================================
"""Compute recursive cumulative sums of a list."""


def moving_cummulative_sum(values):
    """Return an equally sized list of progressive integer sums."""
    if not values:
        return []
    if len(values) == 1:
        return values.copy()
    previous = moving_cummulative_sum(values[:-1])
    return previous + [previous[-1] + values[-1]]


if __name__ == "__main__":
    assert moving_cummulative_sum([5, 6, 7, 1, 2, 3]) == [5, 11, 18, 19, 21, 24]
    print(moving_cummulative_sum([5, 6, 7, 1, 2, 3]))
