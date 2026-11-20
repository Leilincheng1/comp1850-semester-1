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
