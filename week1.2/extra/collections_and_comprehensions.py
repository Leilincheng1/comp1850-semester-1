"""Demonstrate comprehensions, sorting and three collections types."""
from collections import Counter, deque, namedtuple

numbers = [1, 2, 3, 4, 5]
evens = [number for number in numbers if number % 2 == 0]
squares = {number ** 2 for number in numbers}
labels = {number: f"Number {number}" for number in numbers}
print(evens, squares, labels)

items = [5, 1, 4, 2]
print(sorted(items))  # Returns a new, sorted list without changing items.
print(items)
items.sort()  # Sorts the original list in place; returns None.
print(items)

Student = namedtuple("Student", "name grade")
student = Student("Alex", 75)
print(student.name, student.grade)

queue = deque(["first", "second"])
queue.append("third")
print(queue.popleft())

counts = Counter("banana")
print(counts.most_common())
