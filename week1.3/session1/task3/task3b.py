"""Remove fruit items and report normal loop completion."""
fruit = ["apple", "pear", "banana", "orange"]
while fruit:
    print(fruit.pop())
else:
    print("The list is now empty.")
