# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# """Advanced Task 2: Budget Breakdown
# - Ask for three separate expense amounts (for example: travel, food, accommodation).
# - Convert each input so you can add them together to get a total trip cost.
# - Calculate the average spend per category and show each value with an f-string.
# - Extension: format the totals so they always show two decimal places.
# """
#
# travel_cost_input = input("Travel cost in pounds: ")
# food_cost_input = input("Food cost in pounds: ")
# accommodation_cost_input = input("Accommodation cost in pounds: ")
#
# TODO: convert each value to a number type that supports decimals
# TODO: calculate the total and the average spend per category
# TODO: print the three costs, the total, and the average
# Extension: format the totals to two decimal places
# ============================================================================
# Completed solution
# ============================================================================
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
