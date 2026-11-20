# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.2, Session 1: Task 3
#
# fruit = ("apple", "banana", "cherry")
# print(fruit)
#
# Find and display position of "banana"
#
# Display how many times "cherry" occurs
#
# Display how many times "strawberry" occurs
#
# Unpack tuple into variables
# ============================================================================
# Completed solution
# ============================================================================
"""Find, count and unpack entries in a tuple."""
fruit = ("apple", "banana", "cherry")
print(fruit)
print(f"Banana index: {fruit.index('banana')}")
print(f"Cherry count: {fruit.count('cherry')}")
print(f"Strawberry count: {fruit.count('strawberry')}")
first, second, third = fruit
print(first, second, third)
