# `set.intersection()` method

`set.intersection(*others)` returns a **new set** containing only elements present in the original set and **every** other supplied iterable. It takes zero or more iterables as arguments (for example, sets or lists), and does not modify the original set. Calling it with no arguments returns a copy of the original set.

Example program:

```python
python_students = {"Ava", "Ben", "Chen"}
maths_students = {"Ben", "Chen", "Dina"}
both = python_students.intersection(maths_students)
print(sorted(both))  # ['Ben', 'Chen']
print(python_students)  # unchanged
```
