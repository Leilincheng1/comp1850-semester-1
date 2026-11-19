"""Return the sum of a non-empty list, or None for an empty list."""


def process_data(data):
    """Return the sum of integer values, or None for an empty list."""
    if not data:
        return None
    return sum(data)


if __name__ == "__main__":
    print(process_data([1, 2, 3, 4, 5]))
    print(process_data([]))
