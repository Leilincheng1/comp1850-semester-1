# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 4, Session 2: Task 2
#
# We can specify a 2d coordinate point with a tuple p=(x,y)
# Complete two functions to compute the mid-point and distance between 2 points.
# The formula to find the mid point of two points = (x1+x2)/2, y = (y1+y2)/2. Return the midpoint as a point tuple.
# The formula to find the distance between the two points = √((x2 – x1)² + (y2 – y1)²). 
# You can use math.sqrt() to find the square root of a number. 
#
# import math
#
# def midpoint(p1,p2):
    # complete your code here to return a point tuple
#     mid_point = 0
#     return mid_point
#
# def length(p1,p2):
    # complete your code here to return a value
#     distance = 0
#     return distance
#     
#
# Check if correct output is produced
# m = midpoint( (0,0), (4,3) )    # mid = (2.0, 1.5)
# d = length( (0,0), (4,3) )    # dist=5.0
#
# print(f"Distance {d} Midpoint {m}")
# ============================================================================
# Completed solution
# ============================================================================
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
