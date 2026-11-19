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
