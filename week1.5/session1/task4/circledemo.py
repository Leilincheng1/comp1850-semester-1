# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.5, Session 1: Task 4
#
# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py
#
# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle
# ============================================================================
# Completed solution
# ============================================================================
"""Prompt for a circle and show its area and circumference."""
from geometry import Point, Circle


def main():
    """Read centre and radius, then describe the circle."""
    x = float(input("Centre x: "))
    y = float(input("Centre y: "))
    radius = float(input("Radius: "))
    circle = Circle(radius, Point(x, y))
    print(f"Area: {circle.area():.4f}")
    print(f"Perimeter: {circle.perimeter():.4f}")


if __name__ == "__main__":
    main()
