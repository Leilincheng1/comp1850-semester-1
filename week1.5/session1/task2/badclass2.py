# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Another bad class implementation
#
# What does the runtime error mean?
# How do we fix the code?
#
# class Point:
#     """
#     A point in 2D space.
#     """
#
#     def __init__(self, x_coordinate, y_coordinate):
#         """
#         Creates a Point, given x & y coordinates.
#         """
#         x = x_coordinate
#         y = y_coordinate
#
#
# p = Point(1.5, 2.0)
# print(p.x)
# print(p.y)
# ============================================================================
# Completed solution
# ============================================================================
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
