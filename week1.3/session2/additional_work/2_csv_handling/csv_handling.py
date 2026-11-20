# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.3, Additional work: CSV handling
#
# Rewrite the code for average grade task in `session2/task3/2_average_grade/` 
# using `csv.DictReader` to read the data and `csv.DictWriter()` to write to file.
#
# You need to `import csv` to use `csv.DictReader` and `csv.DictWriter()`.
# ============================================================================
# Completed solution
# ============================================================================
"""Use DictReader and DictWriter to export average student grades."""
import csv
from pathlib import Path

folder = Path(__file__).resolve().parents[2] / "task3" / "2_average_grade"
source = folder / "student_data.csv"
output = Path(__file__).parent / "averages.csv"
try:
    with source.open(newline="", encoding="utf-8") as data_file:
        students = list(csv.DictReader(data_file))
    with output.open("w", newline="", encoding="utf-8") as report:
        writer = csv.DictWriter(report, fieldnames=["ID", "Name", "Average"])
        writer.writeheader()
        for student in students:
            average = sum(int(student[key]) for key in
                          ("Mathematics", "Science", "History")) / 3
            writer.writerow({"ID": student["ID"], "Name": student["Name"],
                             "Average": f"{average:.2f}"})
    print(f"Wrote {output}")
except (OSError, KeyError, ValueError) as error:
    print(f"Cannot process CSV data: {error}")
