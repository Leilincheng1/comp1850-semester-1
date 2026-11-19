"""Demonstrate __lt__ and sorted on custom class instances."""


class Student:
    """A student with a comparable numeric result."""

    def __init__(self, name, score):
        """Store a name and score."""
        self.name = name
        self.score = score

    def __lt__(self, other):
        """Sort by score, then by name when scores tie."""
        if not isinstance(other, Student):
            return NotImplemented
        return (self.score, self.name) < (other.score, other.name)

    def __repr__(self):
        """Show a compact representation of the student."""
        return f"Student({self.name!r}, {self.score})"


if __name__ == "__main__":
    students = [Student("Alice", 87), Student("Ben", 65), Student("Carl", 87)]
    print(sorted(students))
    students.sort()
    print(students)
