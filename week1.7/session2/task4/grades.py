# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.7, Session 2: Task 4 - buggy exam grading program
#
# import sys
#
#
# class MarkError(Exception):
#     """
#     Exception raised if an exam mark is not valid.
#
#     To be valid, a mark must be an integer in the range 0-100.
#     """
#
#
# def read_marks(filename):
#     """
#     Given the name of a CSV file, reads student names and exam marks from
#     that file, returning them as a dictionary mapping name onto mark.
#     """
#     with open(filename, "rt") as infile:
#         data = {}
#         infile.readline()  # skip column headings
#         for line in infile:
#             name, mark = line.strip().split(",")
#             data[name] = mark
#         return data
#
#
# def grade(mark):
#     """
#     Given an integer exam mark in the range 0-100, returns a grade of
#     "Fail", "Pass" or "Distinction".
#
#     A mark below 40 is a Fail; a mark of 70 or higher is a Distinction;
#     otherwise the mark is a Pass.
#
#     MarkError is raised if the provided mark is not valid.
#     """
#     if 0 <= mark < 40:
#         return "Fail"
#     elif 40 <= mark <= 70:
#         return "Pass"
#     elif 70 <= mark <= 100:
#         return "Distinction"
#     else:
#         raise MarkError("marks must be in range 0-100")
#
#
# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         sys.exit("Usage: python grades.py <csv-filename>")
#
#     marks = read_marks(sys.argv[1])
#
#     for student, mark in marks.items():
#         student_grade = grade(mark)
#         print(f"{student}: {student_grade}")
# ============================================================================
# Completed solution
# ============================================================================
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
