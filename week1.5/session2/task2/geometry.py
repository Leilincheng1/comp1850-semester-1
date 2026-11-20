"""Points and circles with readable representations."""
import math


class Point:
    """A point in 2D space."""

    def __init__(self, x, y):
        self.x, self.y = x, y

    def distance(self):
        """Return distance from the origin."""
        return math.hypot(self.x, self.y)

    def distance_to(self, p):
        """Return distance to another point."""
        return math.hypot(self.x - p.x, self.y - p.y)

    def __str__(self):
        """Return coordinates in a human-readable string."""
        return f"({self.x}, {self.y})"


class Circle:
    """A circle with a radius and a centre point."""

    def __init__(self, radius, centre=None):
        self.radius = radius
        self.centre = centre if centre is not None else Point(0.0, 0.0)

    def area(self):
        """Return the area."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the circumference."""
        return 2 * math.pi * self.radius

    def __str__(self):
        """Return a string containing centre and radius."""
        return f"Circle(centre={self.centre}, radius={self.radius})"
