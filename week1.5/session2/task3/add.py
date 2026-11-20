# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.5, Session 2: Task 3
#
# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their sum
# ============================================================================
# Completed solution
# ============================================================================
"""Demonstrate the Money class and its addition operator."""
from money import Money

first = Money(1, 99)
second = Money(0, 5)
print(first)
print(second)
print(first + second)
assert str(first + second) == "£2.04"
