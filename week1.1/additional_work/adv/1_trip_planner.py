# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# """Advanced Task 1: Trip Planner
# - Ask for a destination name, total distance in miles, and planned travel time in hours.
# - Convert the numeric inputs so you can calculate an approximate average speed for the journey.
# - Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
# - Extension: warn if either numeric value is zero or negative.
# """
#
# destination = input("Where are you going to? ")
#
# distance_miles_input = input("How many miles will you travel? ")
# time_hours_input = input("How many hours will the journey take? ")
#
# TODO: convert distance_miles_input and time_hours_input to numbers
# TODO: calculate the average speed in miles per hour
# TODO: print a summary message using an f-string
# Extension: add validation for zero or negative values
# ============================================================================
# Completed solution
# ============================================================================
"""Calculate the average speed required for a journey."""

destination = input("Where are you going to? ").strip()
try:
    distance_miles = float(input("How many miles will you travel? "))
    time_hours = float(input("How many hours will the journey take? "))
except ValueError:
    print("Please enter valid numbers for distance and time.")
else:
    if distance_miles <= 0 or time_hours <= 0:
        print("Distance and travel time must both be greater than zero.")
    else:
        average_speed = distance_miles / time_hours
        print(f"Travelling to {destination}: {distance_miles:.2f} miles "
              f"in {time_hours:.2f} hours requires an average speed "
              f"of {average_speed:.2f} mph.")
