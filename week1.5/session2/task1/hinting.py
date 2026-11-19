"""Use type hints to describe numeric Point coordinates (check using mypy)."""
import math


class Point:
    """A point in two-dimensional space."""

    def __init__(self, x: float, y: float) -> None:
        """Store coordinates for the point."""
        self.x: float = x
        self.y: float = y

    def distance(self) -> float:
        """Return the distance from the origin."""
        return math.hypot(self.x, self.y)

    def distance_to(self, p: "Point") -> float:
        """Return the distance to another Point."""
        return math.hypot(self.x - p.x, self.y - p.y)


if __name__ == "__main__":
    point = Point(3.0, 4.0)
    print(point.distance())
    # mypy flags the commented invalid call:
    # invalid = Point("two", "one")
