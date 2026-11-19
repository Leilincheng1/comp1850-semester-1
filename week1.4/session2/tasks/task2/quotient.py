"""Return the quotient and remainder of integer division."""


def divide_and_remainder(dividend, divisor):
    """Return (quotient, remainder) using divmod."""
    return divmod(dividend, divisor)


if __name__ == "__main__":
    quotient, remainder = divide_and_remainder(10, 3)
    print(f"Quotient: {quotient}")
    print(f"Remainder: {remainder}")
    print(divide_and_remainder(33, 3))
