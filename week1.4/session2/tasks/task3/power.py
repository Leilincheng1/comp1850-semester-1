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
