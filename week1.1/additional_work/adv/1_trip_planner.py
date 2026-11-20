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
