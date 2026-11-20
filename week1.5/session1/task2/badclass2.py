"""Correct a constructor that stored local instead of instance variables."""


class Point:
    """Represent a point in 2D space."""

    def __init__(self, x_coordinate, y_coordinate):
        """Store coordinates on self so other methods can access them."""
        self.x = x_coordinate
        self.y = y_coordinate


if __name__ == "__main__":
    p = Point(1.5, 2.0)
    print(p.x)
    print(p.y)
