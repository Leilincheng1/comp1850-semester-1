"""Find the midpoint and distance between Cartesian coordinates."""
import math


def midpoint(p1, p2):
    """Return the arithmetic midpoint of two (x, y) tuples."""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def length(p1, p2):
    """Return the Euclidean distance between two points."""
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


if __name__ == "__main__":
    m = midpoint((0, 0), (4, 3))
    d = length((0, 0), (4, 3))
    print(f"Distance {d} Midpoint {m}")
