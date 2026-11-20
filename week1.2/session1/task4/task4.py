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
