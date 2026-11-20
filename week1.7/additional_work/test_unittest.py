"""Optional Week 1.7 exercise: convert Task 2 tests to unittest.TestCase.

Run with: python -m unittest discover -s week1.7/additional_work -p 'test_*.py'
"""
import sys
import unittest
from pathlib import Path

# Each Task 2 example lives in a separate folder rather than a package.
TASK2 = Path(__file__).resolve().parents[1] / "session1" / "task2"
sys.path.insert(0, str(TASK2 / "1_weather"))
sys.path.insert(0, str(TASK2 / "2_process_data"))
sys.path.insert(0, str(TASK2 / "3_geometry"))

from weather import comfort_level
from process_data import process_data
from geometry import Point, Circle
import math


class WeatherTests(unittest.TestCase):
    """Exercise the equivalence classes for comfort_level."""

    def test_cold(self):
        self.assertEqual(comfort_level(15), "COLD")
        self.assertEqual(comfort_level(-5), "COLD")

    def test_ok(self):
        self.assertEqual(comfort_level(15.1), "OK")
        self.assertEqual(comfort_level(25), "OK")

    def test_hot(self):
        self.assertEqual(comfort_level(25.1), "HOT")


class ProcessDataTests(unittest.TestCase):
    """Exercise empty, singleton, positive and negative lists."""

    def test_empty(self):
        self.assertIsNone(process_data([]))

    def test_singleton(self):
        self.assertEqual(process_data([-7]), -7)

    def test_multiple(self):
        self.assertEqual(process_data([5, -2, 3]), 6)


class GeometryTests(unittest.TestCase):
    """Exercise Point and Circle methods."""

    def test_point_constructor(self):
        point = Point(3, 4)
        self.assertEqual((point.x, point.y), (3, 4))

    def test_point_distance(self):
        self.assertEqual(Point(3, 4).distance(), 5)

    def test_point_distance_to(self):
        self.assertEqual(Point(0, 0).distance_to(Point(3, 4)), 5)

    def test_circle_constructor(self):
        circle = Circle(2)
        self.assertEqual(circle.radius, 2)
        self.assertEqual((circle.centre.x, circle.centre.y), (0, 0))

    def test_circle_area(self):
        self.assertAlmostEqual(Circle(2).area(), 4 * math.pi)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(Circle(2).perimeter(), 4 * math.pi)


if __name__ == "__main__":
    unittest.main()
