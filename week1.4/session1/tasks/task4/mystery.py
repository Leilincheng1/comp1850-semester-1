# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 4, Session 1
#
# You are given the function mystery_func. 
# Inspect the code in the function
# Your task is to write a corresponding docstring
# - what the function does 
# - what is the input data and type
# - what is the return value and type
#
#
# function implementation
#
# def mystery_func(string):
#     upper = 0
#     lower = 0
#
#     for ch in string:
#         if ch.isupper():
#             upper += 1
#         if ch.islower():
#             lower += 1
#     return (upper, lower)
#
#
# testing
#
# print(mystery_func("abc"))
# print(mystery_func("The quick Brown Fox!"))
# print(mystery_func("012345"))
# print(mystery_func("ABC"))
#
#
# Can you predict the output of the following lines of code?
# Uncomment the lines of code one by one and run the program
# to see if you are right?
#
# print(mystery_func("X"))
# print(mystery_func("[2, 3]"))
# ============================================================================
# Completed solution
# ============================================================================
"""Count the upper- and lowercase letters in a string."""


def mystery_func(string):
    """Return (uppercase_count, lowercase_count) for the provided string.

    Args:
        string (str): Characters to examine.

    Returns:
        tuple[int, int]: Counts of uppercase and lowercase letters;
        digits and punctuation are ignored.
    """
    upper, lower = 0, 0
    for character in string:
        if character.isupper():
            upper += 1
        if character.islower():
            lower += 1
    return upper, lower


if __name__ == "__main__":
    for value in ("abc", "The quick Brown Fox!", "012345", "ABC", "X", "[2, 3]"):
        print(mystery_func(value))
