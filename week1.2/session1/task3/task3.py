"""Find, count and unpack entries in a tuple."""
fruit = ("apple", "banana", "cherry")
print(fruit)
print(f"Banana index: {fruit.index('banana')}")
print(f"Cherry count: {fruit.count('cherry')}")
print(f"Strawberry count: {fruit.count('strawberry')}")
first, second, third = fruit
print(first, second, third)
