# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.2, Session 1: Task 4
#
# fruit = {"apple", "orange", "tomato"}
# vegetables = {"leek", "tomato", "potato"}
#
# What do you think will be printed here?
#
# both = fruit.intersection(vegetables)
# print(both)
#
# Why does the following code diplay five items?
#
# food = fruit.union(vegetables)
# print(food)
#
# Add an item to fruit
#
# Remove an item from vegetables
#
# Find and display symmetric difference of the two sets
# ============================================================================
# Completed solution
# ============================================================================
"""Explore set intersection, union and symmetric difference."""
fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}
both = fruit.intersection(vegetables)
print(both)
food = fruit.union(vegetables)
print(food)
fruit.add("banana")
print(fruit)
vegetables.remove("leek")
print(vegetables)
print(fruit.symmetric_difference(vegetables))
