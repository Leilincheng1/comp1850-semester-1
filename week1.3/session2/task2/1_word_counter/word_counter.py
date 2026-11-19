"""Read a text file and count its whitespace-separated words."""
from pathlib import Path

filename = input("Enter a text filename: ")
path = Path(__file__).parent / filename
try:
    content = path.read_text(encoding="utf-8")
except OSError as error:
    print(f"Unable to read file: {error}")
else:
    print(f"Word count: {len(content.split())}")
