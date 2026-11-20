"""Read exam marks from CSV and classify each student's result."""
import sys


class MarkError(Exception):
    """Raised when an exam mark is not an integer between 0 and 100."""


def read_marks(filename):
    """Return student names mapped to integer marks from a CSV file."""
    with open(filename, "rt", encoding="utf-8") as infile:
        data = {}
        infile.readline()  # Skip column headings.
        for line in infile:
            name, mark = line.strip().split(",")
            data[name] = int(mark)
        return data


def grade(mark):
    """Classify a valid integer mark or raise MarkError for invalid input."""
    if type(mark) is not int or not 0 <= mark <= 100:
        raise MarkError("marks must be integers in range 0-100")
    if mark < 40:
        return "Fail"
    if mark < 70:
        return "Pass"
    return "Distinction"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python grades.py <csv-filename>")

    marks = read_marks(sys.argv[1])
    for student, mark in marks.items():
        print(f"{student}: {grade(mark)}")
