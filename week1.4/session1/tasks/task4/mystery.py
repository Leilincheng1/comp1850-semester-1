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
