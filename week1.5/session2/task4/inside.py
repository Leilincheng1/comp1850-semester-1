# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.5, Session 2: Task 4
#
# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
# ============================================================================
# Completed solution
# ============================================================================
"""Demonstrate whether points fall inside a circle."""
from geometry import Point, Circle

circle = Circle(5, Point(0, 0))
for point in (Point(0, 0), Point(3, 4), Point(6, 0)):
    print(f"{point}: {'inside' if point in circle else 'outside'}")
