"""Shapes with validated positions, colours and dimensions."""
import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """Superclass for shapes with a point and colour."""

    def __init__(self, position, colour):
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """Move the shape to the supplied Point."""
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")
        self.position = position

    def set_colour(self, colour):
        """Change the colour, rejecting unsupported names."""
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")
        self.colour = colour


class Circle(Shape):
    """Circle inheriting position and colour from Shape."""

    def __init__(self, radius, position, colour="red"):
        """Create a circle with validated dimensions, position and colour."""
        super().__init__(position, colour)
        self.set_radius(radius)

    def set_radius(self, radius):
        """Set a positive numeric radius."""
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        if radius <= 0:
            raise ValueError("radius must be greater than zero")
        self.radius = radius

    def __str__(self):
        """Display colour, radius and position."""
        return f"{self.colour} circle, radius {self.radius}, at {self.position}"

    def area(self):
        """Return the area of this circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the circumference of this circle."""
        return 2 * math.pi * self.radius
