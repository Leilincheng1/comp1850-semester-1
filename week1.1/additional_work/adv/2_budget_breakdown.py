"""Show a trip's expenses, total cost and average category cost."""

try:
    travel = float(input("Travel cost in pounds: "))
    food = float(input("Food cost in pounds: "))
    accommodation = float(input("Accommodation cost in pounds: "))
except ValueError:
    print("Please enter valid numbers for all three costs.")
else:
    total = travel + food + accommodation
    average = total / 3
    print(f"Travel: £{travel:.2f}")
    print(f"Food: £{food:.2f}")
    print(f"Accommodation: £{accommodation:.2f}")
    print(f"Total: £{total:.2f}")
    print(f"Average per category: £{average:.2f}")
