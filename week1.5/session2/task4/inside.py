"""Demonstrate whether points fall inside a circle."""
from geometry import Point, Circle

circle = Circle(5, Point(0, 0))
for point in (Point(0, 0), Point(3, 4), Point(6, 0)):
    print(f"{point}: {'inside' if point in circle else 'outside'}")
