"""Calculate circle area with an optional approximation of pi."""


def circle_area(radius, pi_value=3.142):
    """Return pi times radius squared."""
    return pi_value * radius * radius


if __name__ == "__main__":
    for radius in (2, 5, 22.5):
        print(circle_area(radius))
