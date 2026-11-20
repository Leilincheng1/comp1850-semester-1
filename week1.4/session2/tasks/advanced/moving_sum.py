"""Compute recursive cumulative sums of a list."""


def moving_cummulative_sum(values):
    """Return an equally sized list of progressive integer sums."""
    if not values:
        return []
    if len(values) == 1:
        return values.copy()
    previous = moving_cummulative_sum(values[:-1])
    return previous + [previous[-1] + values[-1]]


if __name__ == "__main__":
    assert moving_cummulative_sum([5, 6, 7, 1, 2, 3]) == [5, 11, 18, 19, 21, 24]
    print(moving_cummulative_sum([5, 6, 7, 1, 2, 3]))
