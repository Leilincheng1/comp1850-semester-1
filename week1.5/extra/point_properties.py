"""A Point whose coordinates are validated by property setters."""
import math


class Point:
    """A point with protected numeric coordinates."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        """Return horizontal position."""
        return self._x

    @x.setter
    def x(self, value):
        """Allow only numeric horizontal coordinates."""
        if type(value) not in (int, float):
            raise TypeError("x must be numeric")
        self._x = value

    @property
    def y(self):
        """Return vertical position."""
        return self._y

    @y.setter
    def y(self, value):
        """Allow only numeric vertical coordinates."""
        if type(value) not in (int, float):
            raise TypeError("y must be numeric")
        self._y = value

    def distance(self):
        """Return distance from origin."""
        return math.hypot(self.x, self.y)


if __name__ == "__main__":
    point = Point(3, 4)
    print(point.distance())
    point.x = 6
    try:
        point.y = "invalid"
    except TypeError as error:
        print(error)
