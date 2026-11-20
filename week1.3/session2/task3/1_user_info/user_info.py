# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.3, Session 2: Write User Information to a File
#
#
# Prompt the user for their name, age, and favorite colour.
#
# Open a file called 'user_info.txt' for reading
#
# Write each piece of information to the file, each on a new line.
#
# Hints:
# - Remember to add \n for new lines when writing to files
#
#
# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
# ============================================================================
# Completed solution
# ============================================================================
"""Append user information to a text file, one field per line."""
from pathlib import Path

output = Path(__file__).parent / "user_info.txt"
while True:
    name = input("Name (blank to finish): ").strip()
    if not name:
        break
    age = input("Age: ").strip()
    colour = input("Favourite colour: ").strip()
    with output.open("a", encoding="utf-8") as file:
        file.write(f"Name: {name}\nAge: {age}\nFavourite colour: {colour}\n\n")
    print("Saved.")
