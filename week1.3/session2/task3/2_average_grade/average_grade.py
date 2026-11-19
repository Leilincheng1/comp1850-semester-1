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
