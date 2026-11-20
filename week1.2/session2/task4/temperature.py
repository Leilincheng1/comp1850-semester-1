"""Classify a Celsius temperature."""
temperature = float(input("Enter the temperature in Celsius: "))
if temperature < 10:
    print(f"{temperature}°C is cold.")
elif temperature < 23:
    print(f"{temperature}°C is warm.")
else:
    print(f"{temperature}°C is hot.")
