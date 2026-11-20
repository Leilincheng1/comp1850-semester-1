# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.2, Session 1: Task 1
#
# Create a shopping list
#
# shopping = ["eggs", "milk", "flour", "carrots"]
# print(shopping)
#
# We forgot something, so add it to list
#
# shopping.append("bananas")
# print(shopping)
#
# We bought something, so remove it from list
#
# shopping.remove("eggs")
# print(shopping)
#
# Replace bananas with grapes
#
# Add yoghurt, just after milk
# ============================================================================
# Completed solution
# ============================================================================
"""Update a shopping list by replacement and insertion."""
shopping = ["eggs", "milk", "flour", "carrots"]
print(shopping)
shopping.append("bananas")
print(shopping)
shopping.remove("eggs")
print(shopping)
shopping[shopping.index("bananas")] = "grapes"
print(shopping)
shopping.insert(shopping.index("milk") + 1, "yoghurt")
print(shopping)
