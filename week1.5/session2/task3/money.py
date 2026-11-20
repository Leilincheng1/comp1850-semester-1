# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.5, Session 2: Task 3
#
# class Money:
#     """
#     An amount of money, in British Pounds Sterling.
#     """
#
#     def __init__(self, pounds, pence):
#         """
#         Creates a Money object, given the number of pounds and pence.
#         """
        # Add validation code here, to check that
        # - the pounds parameter is an integer
        # - pounds is not negative
        # - the pence parameter is an integer
        # - pence is not negative and not greater than 99
        # Raise appropriate exceptions if any of these are violated
#
#         self.pounds = pounds
#         self.pence = pence
#
#     def __str__(self):
#         """
#         Returns a string representation of this Money.
#         """
        # Add code here to return an appropriate string representation
        # Use the currency symbol for British Pounds Sterling
        # Represent pence with a leading zero if needed (e.g. '05')
#
#     def __add__(self, other):
#         """
#         Adds this Money to another Money, returning the total.
#         """
        # Add code here to check that parameter 'other' is a Money object,
        # add self to other, then return the sum as a new Money object
        # (see README for hints and tips)
# ============================================================================
# Completed solution
# ============================================================================
"""Store and add nonnegative amounts of pounds sterling."""


class Money:
    """An amount of money in pounds and pence."""

    def __init__(self, pounds, pence):
        """Validate and store a currency amount."""
        if type(pounds) is not int:
            raise TypeError("pounds must be an integer")
        if type(pence) is not int:
            raise TypeError("pence must be an integer")
        if pounds < 0:
            raise ValueError("pounds must be >= 0")
        if not 0 <= pence <= 99:
            raise ValueError("pence must be in range 0-99")
        self.pounds, self.pence = pounds, pence

    def __str__(self):
        """Return the amount as a pounds-and-pence currency string."""
        return f"£{self.pounds}.{self.pence:02d}"

    def __add__(self, other):
        """Return a new Money holding the sum of two Money objects."""
        if not isinstance(other, Money):
            raise TypeError("other object must be a Money")
        total_pence = self.pence + other.pence
        return Money(self.pounds + other.pounds + total_pence // 100, total_pence % 100)
