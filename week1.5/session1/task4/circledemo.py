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
