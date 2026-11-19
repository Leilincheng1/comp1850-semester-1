"""Classes for working with two-dimensional geometry."""
import math


class Point:
    """A point in two-dimensional Cartesian space."""

    def __init__(self, x, y):
        """Store x and y coordinates."""
        self.x = x
        self.y = y

    def distance(self):
        """Return the distance from this point to the origin."""
        return math.hypot(self.x, self.y)

    def distance_to(self, other):
        """Return the Euclidean distance to another Point."""
        return math.hypot(self.x - other.x, self.y - other.y)


class Circle:
    """A circle with a radius and a Point centre."""

    def __init__(self, radius, centre=None):
        """Initialize radius and centre (origin by default)."""
        self.radius = radius
        self.centre = centre if centre is not None else Point(0.0, 0.0)

    def area(self):
        """Return the circle's area."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the circle's circumference."""
        return 2 * math.pi * self.radius
