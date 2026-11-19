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
