# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.5, Session 2: Task 2
#
# """
# Classes for working with two-dimensional geometry.
# """
#
# import math
#
#
# class Point:
#     """
#     A point in 2D space.
#     """
#
#     def __init__(self, x, y):
#         """
#         Creates a Point, given x & y coordinates.
#         """
#         self.x = x
#         self.y = y
#
#     def distance(self):
#         """
#         Returns distance of this Point from the origin.
#         """
#         return math.hypot(self.x, self.y)
#
#     def distance_to(self, p):
#         """
#         Returns distance of this Point from another Point.
#         """
#         return math.hypot(self.x - p.x, self.y - p.y)
#
    # Implement a __str__() method here
#
#
# class Circle:
#     """
#     A circle, with a radius and centre coordinates.
#     """
#
#     def __init__(self, radius, centre=Point(0.0, 0.0)):
#         """
#         Creates a Circle, given values for radius & centre coordinates.
#
#         Radius must always be supplied. Centre coordinates are optional
#         but should be provided as a Point object. If they are omitted, the
#         circle will be centred at the origin.
#         """
#         self.radius = radius
#         self.centre = centre
#
#     def area(self):
#         """
#         Returns the area of this Circle.
#         """
#         return math.pi * self.radius * self.radius
#
#     def perimeter(self):
#         """
#         Returns the perimeter of this Circle.
#         """
#         return 2.0 * math.pi * self.radius
#
    # Implement a __str__() method here
# ============================================================================
# Completed solution
# ============================================================================
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
