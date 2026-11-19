"""Classify a numeric grade for COMP1850 Worksheet 1.2."""
import sys

raw_grade = input("Enter a grade (0-100): ")
if not raw_grade.isdecimal():
    sys.exit("Error: Grade must be an integer between 0 and 100")

grade = int(raw_grade)
if not 0 <= grade <= 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if grade < 40:
    result = "Fail"
elif grade < 70:
    result = "Pass"
else:
    result = "Distinction"

print(f"{grade} is a {result}")
