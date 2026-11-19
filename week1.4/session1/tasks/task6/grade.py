"""Convert valid numeric marks to letter grades."""


def calculate_grade(marks):
    """Return A, B, C, D, F, or None for invalid marks."""
    if type(marks) is not int or not 0 <= marks <= 100:
        return None
    if marks < 50:
        return "F"
    if marks < 60:
        return "D"
    if marks < 70:
        return "C"
    if marks < 80:
        return "B"
    return "A"


if __name__ == "__main__":
    for mark in (39, 55, -20, 100):
        print(calculate_grade(mark))
