"""Count odd and even integers in a list."""


def odd_even(lstIntegers):
    """Return [odd_count, even_count]."""
    odd = sum(value % 2 != 0 for value in lstIntegers)
    return [odd, len(lstIntegers) - odd]


if __name__ == "__main__":
    print(odd_even([1, 2, 3, 4, 5]))
