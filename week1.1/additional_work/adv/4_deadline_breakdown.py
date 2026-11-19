"""Break a positive number of minutes down into days, hours and minutes."""

try:
    minutes_remaining = int(input("Minutes remaining until the deadline: "))
except ValueError:
    print("Please enter a whole number of minutes.")
else:
    if minutes_remaining < 0:
        print("Warning: the deadline has already passed.")
    else:
        days = minutes_remaining // 1440
        hours = (minutes_remaining % 1440) // 60
        minutes = minutes_remaining % 60
        print(f"{days} days, {hours} hours, {minutes} minutes remaining")
