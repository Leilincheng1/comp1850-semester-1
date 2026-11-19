"""Compute descriptive statistics without loops for COMP1850 Worksheet 1.2."""
import sys
from util import read_numbers

numbers = read_numbers()
if not numbers:
    sys.exit("Error: no numbers provided")

numbers.sort()
count = len(numbers)
minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / count
middle = count // 2
median = (numbers[middle] if count % 2 else
          (numbers[middle - 1] + numbers[middle]) / 2)

print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print(f"Mean = {mean}")
print(f"Median = {median}")
