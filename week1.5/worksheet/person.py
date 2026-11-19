"""Person class for COMP1850 Worksheet 1.5."""
from datetime import date


class Person:
    """A person with a name and date of birth."""

    def __init__(self, name, birth):
        """Validate and store the person's name and date of birth."""
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name:
            raise ValueError("name must not be empty")
        if not isinstance(birth, date):
            raise TypeError("birth must be a date")
        self.name = name
        self.birth = birth

    def initials(self):
        """Return the uppercase initials of each word in the name."""
        return "".join(part[0].upper() for part in self.name.split())

    def is_birthday(self):
        """Return whether today has the person's birth month and day."""
        today = date.today()
        return (today.month, today.day) == (self.birth.month, self.birth.day)
