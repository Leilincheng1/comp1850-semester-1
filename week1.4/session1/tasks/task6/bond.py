"""Detect a subsequence of 0, 0, 7 in a list of integers."""


def isBond(intList):
    """Return True if 0, 0, 7 appear in order, not necessarily consecutively."""
    expected = (0, 0, 7)
    next_index = 0
    for value in intList:
        if value == expected[next_index]:
            next_index += 1
            if next_index == len(expected):
                return True
    return False


if __name__ == "__main__":
    print(isBond([1, 2, 4, 0, 0, 7, 5]))
    print(isBond([1, 0, 2, 4, 0, 5, 7]))
    print(isBond([1, 7, 2, 0, 4, 5, 0]))
