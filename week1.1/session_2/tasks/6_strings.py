# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does
#
# user_string = input("Enter a string: ")
#
# print(f"\nOriginal String: {user_string}")
# print(f"Modified String 1: {user_string.lower()}")
# print(f"Modified String 2: {user_string.upper()}")
# print(f"Modified String 3: {user_string.strip()}")
# print(f"Modified String 4: {user_string.replace('a', '@')}")
# print(f"Modified String 5: {user_string.capitalize()}")
# print(f"Modified String 6: {user_string[::-1]}")
# print(f"Modified String 7: {user_string.title()}")
# print(f"Modified String 8: {len(user_string)}")
# print(f"Modified String 9: {user_string.find('a')}")
# print(f"Modified String 10: {user_string.count('a')}")
# print(f"Modified String 11: {user_string.startswith('Hello')}")
# print(f"Modified String 12: {user_string.endswith('!')}")
# print(f"Modified String 13: {user_string.isalnum()}")
# print(f"Modified String 14: {user_string.isalpha()}")
# print(f"Modified String 15: {user_string.isdigit()}")
#
#
#
######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!
# ============================================================================
# Completed solution
# ============================================================================
"""Explore common Python string operations and their results."""

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
print(f"Modified String 1: {user_string.lower()}")  # Convert letters to lowercase.
print(f"Modified String 2: {user_string.upper()}")  # Convert letters to uppercase.
print(f"Modified String 3: {user_string.strip()}")  # Remove whitespace at both ends.
print(f"Modified String 4: {user_string.replace('a', '@')}")  # Replace every lowercase 'a'.
print(f"Modified String 5: {user_string.capitalize()}")  # Uppercase first letter and lowercase the rest.
print(f"Modified String 6: {user_string[::-1]}")  # Reverse the string using slicing.
print(f"Modified String 7: {user_string.title()}")  # Capitalize the start of each word.
print(f"Modified String 8: {len(user_string)}")  # Count all characters, including spaces.
print(f"Modified String 9: {user_string.find('a')}")  # Find first 'a', or -1 if absent.
print(f"Modified String 10: {user_string.count('a')}")  # Count lowercase 'a' occurrences.
print(f"Modified String 11: {user_string.startswith('Hello')}")  # Test the prefix (case-sensitive).
print(f"Modified String 12: {user_string.endswith('!')}")  # Test the suffix.
print(f"Modified String 13: {user_string.isalnum()}")  # True for nonempty letters/digits only.
print(f"Modified String 14: {user_string.isalpha()}")  # True for nonempty letters only.
print(f"Modified String 15: {user_string.isdigit()}")  # True for nonempty numeric digits only.

# Additional methods: split into words and count words.
print(f"Words: {user_string.split()}")
print(f"Word count: {len(user_string.split())}")
