"""Pop items from a list until it is empty."""
fruit = ["apple", "pear", "banana", "orange"]
# First iteration: orange removed, leaving apple/pear/banana.
# Fourth iteration: apple removed, leaving [].
# After the loop: []. Empty lists are false in Boolean contexts.
while fruit:
    print(fruit.pop())
