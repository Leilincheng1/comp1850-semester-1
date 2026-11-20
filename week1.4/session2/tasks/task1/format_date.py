"""Format a date using a custom optional separator."""


def format_date(day, month, year, separator="-"):
    """Return day, month and year joined by separator."""
    return f"{day}{separator}{month}{separator}{year}"


# Keep the original template spelling available as well.
format_data = format_date

if __name__ == "__main__":
    for separator in ("-", "/", ":", "."):
        print(format_date(19, 11, 2026, separator))
