"""Count case-insensitive letter frequencies in a text file."""
from collections import Counter
from pathlib import Path

filename = input("File to analyse [code.txt]: ").strip() or "code.txt"
try:
    content = (Path(__file__).parent / filename).read_text(encoding="utf-8")
except OSError as error:
    print(f"Cannot read file: {error}")
else:
    frequency = Counter(character.lower() for character in content if character.isalpha())
    print(dict(sorted(frequency.items())))
