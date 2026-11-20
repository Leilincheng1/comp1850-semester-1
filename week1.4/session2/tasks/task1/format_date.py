# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 4, Session 2: Task 1
#
# Write a function format_date that takes 4 arguments: day, month,
# year, separator. The separator is an optional argument with a default
# value to be "-". The function returns the formatted date as a string
# in the format day-month-year with the default separator.
#
#
# def format_data(day, month, year, separator):
    # complete your code here
#
#     return formatted_date
#
#
# Write code to test the function with separators such as "/", ":", "."
# ============================================================================
# Completed solution
# ============================================================================
"""Format a date using a custom optional separator."""


def format_date(day, month, year, separator="-"):
    """Return day, month and year joined by separator."""
    return f"{day}{separator}{month}{separator}{year}"


# Keep the original template spelling available as well.
format_data = format_date

if __name__ == "__main__":
    for separator in ("-", "/", ":", "."):
        print(format_date(19, 11, 2026, separator))
