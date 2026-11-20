# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.3, Session 2: Calculate Average Grade and Write to a File
#
# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]
#
#
# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3
#
#
# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
# ============================================================================
# Completed solution
# ============================================================================
"""Write each student's mean mark to a text report."""
import csv
from pathlib import Path

folder = Path(__file__).parent
try:
    with (folder / "student_data.csv").open(newline="", encoding="utf-8") as source:
        students = list(csv.DictReader(source))
    with (folder / "report.txt").open("w", encoding="utf-8") as output:
        for student in students:
            marks = [int(student[field]) for field in ("Mathematics", "Science", "History")]
            output.write(f"{student['Name']}: {sum(marks) / 3:.2f}\n")
    print("Saved report.txt")
except (OSError, ValueError, KeyError) as error:
    print(f"Unable to produce report: {error}")
