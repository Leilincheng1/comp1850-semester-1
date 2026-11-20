"""Compare calendar formatting options."""
import calendar

if __name__ == "__main__":
    print(calendar.month(2025, 10))
    print(calendar.month(2025, 10, w=3, l=1))
    print(calendar.month(2025, 10, w=4, l=2))
    print(calendar.calendar(2025, w=2, l=1, c=6, m=3))
    print(calendar.calendar(2025, w=3, l=1, c=4, m=4))
    print(calendar.calendar(2025, w=2, l=2, c=8, m=2))
