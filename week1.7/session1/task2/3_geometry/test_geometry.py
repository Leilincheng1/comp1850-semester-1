"""Unit tests for Point and Circle geometry methods."""
import math
import pytest
from geometry import Point, Circle


def test_point_constructor():
    point = Point(5, -2)
    assert point.x == 5
    assert point.y == -2


def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0


def test_point_distance_to():
    origin = Point(0, 0)
    point = Point(3, 4)
    assert origin.distance_to(point) == 5.0
    assert point.distance_to(origin) == 5.0
    assert point.distance_to(point) == 0.0


def test_circle_constructor():
    circle = Circle(3)
    assert circle.radius == 3
    assert circle.centre.x == 0.0
    assert circle.centre.y == 0.0
    custom_centre = Point(2, -5)
    other = Circle(4, custom_centre)
    assert other.radius == 4
    assert other.centre is custom_centre


def test_circle_area():
    assert Circle(0).area() == 0.0
    assert Circle(3).area() == pytest.approx(9 * math.pi)


def test_circle_perimeter():
    assert Circle(0).perimeter() == 0.0
    assert Circle(3).perimeter() == pytest.approx(6 * math.pi)
