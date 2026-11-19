def countdown(number):
    """Recursively print each integer from number down to zero."""
    if number < 0:
        raise ValueError("The starting number must be non-negative.")
    print(number)
    if number > 0:
        countdown(number - 1)
