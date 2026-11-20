# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.3, Session 2: Word Counter
#
# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.
#
# open and read the file
#
# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings
#
# display the wordcount
#
# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210
# ============================================================================
# Completed solution
# ============================================================================
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
