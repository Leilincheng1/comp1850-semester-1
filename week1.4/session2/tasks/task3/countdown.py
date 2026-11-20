# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 4, Session 2: 
#
# Given incomplete recursive function countdown with a docstring.
# Your task is to complete the function based on the details in the docstring.
#
# def countdown(n):
#     """
#     This recursive function prints numbers from n down to 0.
#
#     Args:
#         n : int, positive integer representing the starting number.
#
#     Returns:
#         None, prints the countdown sequence from n to 0.
#     """
#
    # Complete your code here
    # base case
#
    # recursive case
#
#
# check if correct output is produced
# countdown(30)    # 30 ... 0 (Note: each number is printed in a separate line)
# countdown(5)     # 5 ... 0  (Note: each number in printed in a separate line)
#
#
# Once you have completed, your next task is to write an equivalent function that
# uses a loop.
# ============================================================================
# Completed solution
# ============================================================================
"""Print a descending sequence recursively and iteratively."""


def countdown(n):
    """Print integers from n to zero using recursion."""
    if n < 0:
        return
    print(n)
    countdown(n - 1)


def countdown_loop(n):
    """Print the same countdown using a for loop."""
    for number in range(n, -1, -1):
        print(number)


if __name__ == "__main__":
    countdown(30)
    countdown(5)
    countdown_loop(5)
