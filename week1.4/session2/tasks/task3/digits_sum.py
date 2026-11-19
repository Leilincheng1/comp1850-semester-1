"""Sum the digits of a nonnegative integer recursively and iteratively."""


def digits_sum(number):
    """Return the sum of decimal digits via recursion."""
    if number < 10:
        return number
    return number % 10 + digits_sum(number // 10)


def digits_sum_loop(number):
    """Return digit sum using a while loop."""
    total = 0
    while number:
        total += number % 10
        number //= 10
    return total


if __name__ == "__main__":
    for value in (987, 12345):
        print(digits_sum(value))
        assert digits_sum(value) == digits_sum_loop(value)
