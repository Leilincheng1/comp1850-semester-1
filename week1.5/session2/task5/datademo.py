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
