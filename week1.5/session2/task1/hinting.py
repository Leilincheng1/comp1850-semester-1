# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.5, Session 2: Task 1
#
# Add type hints to the Point class
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
#         Returns distance of this Point from the specified Point.
#         """
#         return math.hypot(self.x - p.x, self.y - p.y)
#
#
# Test program
#
# p = Point("two", "one")
# print(p.distance())
# ============================================================================
# Completed solution
# ============================================================================
"""Use type hints to describe numeric Point coordinates (check using mypy)."""
import math
from typing import TYPE_CHECKING


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
    # This branch is statically checked by mypy but not run by Python.
    # It demonstrates the exact incompatible argument types from the task.
    if TYPE_CHECKING:
        invalid = Point("two", "one")
