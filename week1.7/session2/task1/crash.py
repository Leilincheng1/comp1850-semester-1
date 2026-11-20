"""Assign squares to each element without exceeding the list's bounds."""


def assign_values(values):
    """Replace each list item with its 1-based index squared."""
    for i in range(len(values)):
        values[i] = (i + 1) ** 2


if __name__ == "__main__":
    data = [0] * 10
    assign_values(data)
    print("Done!")
    print(data)
