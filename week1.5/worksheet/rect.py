"""Rectangle class for COMP1850 Worksheet 1.5."""


class Rectangle:
    """A rectangle with positive integer width and height."""

    def __init__(self, width, height):
        """Store the dimensions, rejecting invalid types and values."""
        if type(width) is not int or type(height) is not int:
            raise TypeError("width and height must be integers")
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")
        self.width = width
        self.height = height

    def is_square(self):
        """Return True when the width and height are equal."""
        return self.width == self.height

    def area(self):
        """Return the area of this rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the length of the rectangle's boundary."""
        return 2 * (self.width + self.height)
