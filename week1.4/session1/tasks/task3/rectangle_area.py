# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
#
# function implementation
#
# def rectangle_area( ):  # define suitable input data
    # ...               # implement the function
#     return              # return an appropriate value
#
# testing the function
#
# print(f"Area is {rectangle_area( )}")   # provide suitable data matching your inputs
# ============================================================================
# Completed solution
# ============================================================================
"""Three introductory functions and simple tests."""


def rectangle_area(width, height):
    """Return the area of a rectangle."""
    return width * height


def even_numbers(limit):
    """Return the even integers from zero up to the supplied integer."""
    return list(range(0, limit + 1, 2))


def mean(numbers):
    """Return the arithmetic mean or None when the list is empty."""
    return sum(numbers) / len(numbers) if numbers else None


if __name__ == "__main__":
    print(f"Area is {rectangle_area(4, 6)}")
    print(even_numbers(12))
    print(mean([2, 4, 6]))
    assert rectangle_area(4, 6) == 24
    assert even_numbers(5) == [0, 2, 4]
    assert mean([2, 4, 6]) == 4
