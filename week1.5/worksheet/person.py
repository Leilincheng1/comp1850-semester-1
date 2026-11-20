# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Worksheet 1.5: Person class
#
# from datetime import date
#
# class Person:
#     """
#     A Person, with a name and a date of birth.
#     """
#
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
#
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
# ============================================================================
# Completed solution
# ============================================================================
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
from datetime import date


class Person:
    """A person with a name and a date of birth."""

    def __init__(self, name, birth):
        """Create a person with the given name and date of birth."""
        if not isinstance(name, str):
            raise TypeError("name must be a string")

        if name == "":
            raise ValueError("name must not be empty")

        if not isinstance(birth, date):
            raise TypeError("birth must be a date")

        self.name = name
        self.birth = birth

    def initials(self):
        """Return the uppercase initial of each part of the person's name."""
        return "".join(part[0].upper() for part in self.name.split())

    def is_birthday(self):
        """Return True if today is the person's birthday, and False otherwise."""
        today = date.today()
        return today.month == self.birth.month and today.day == self.birth.day
