# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.5, Session 1: Task 3
#
# class Point:
#     """
#     A Point in 2D space.
#     """
#
    # Add constructor here
#
    # Add distance() method here
#
    # Add distance_to() method here
    # (This will need a parameter representing another point)
#
#
#
# Finally, add code here to demonstrate use of Point
# ============================================================================
# Completed solution
# ============================================================================
"""Demonstrate distances between two-dimensional points."""
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


if __name__ == "__main__":
    first = Point(3, 4)
    second = Point(6, 8)
    print(f"First point: ({first.x}, {first.y})")
    print(f"Distance from origin: {first.distance()}")
    print(f"Distance between points: {first.distance_to(second)}")
