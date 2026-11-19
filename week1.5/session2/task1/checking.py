"""Runtime checks reject nonnumeric Point coordinates."""
import math


class Point:
    """A point in two-dimensional space."""

    def __init__(self, x, y):
        """Reject invalid types when the object is constructed."""
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Point coordinates must be int or float")
        self.x, self.y = x, y

    def distance(self):
        """Return distance from the origin."""
        return math.hypot(self.x, self.y)

    def distance_to(self, p):
        """Return distance to another point."""
        return math.hypot(self.x - p.x, self.y - p.y)


if __name__ == "__main__":
    try:
        Point("two", "one")
    except TypeError as error:
        print(f"Expected invalid-coordinate error: {error}")
    print(Point(3, 4).distance())
