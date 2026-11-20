# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.5, Session 2: Task 5
#
# Write a program here to create a Dataset containing data
# from a file named by the user
#
# Your program should display dataset size, mean and median,
# followed by the individual values (using a for loop)
# ============================================================================
# Completed solution
# ============================================================================
"""Demonstrate the public Dataset API on a named data file."""
from pathlib import Path
from data import Dataset

filename = input("Enter the data filename: ").strip()
dataset = Dataset(Path(__file__).parent / filename)
print(f"Size: {len(dataset)}")
print(f"Mean: {dataset.mean()}")
print(f"Median: {dataset.median()}")
for value in dataset:
    print(value)
