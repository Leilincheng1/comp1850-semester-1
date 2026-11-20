"""Convert valid Celsius temperatures into Fahrenheit."""


def valid_temperature(temperature):
    """Check whether temperature is between -100 and 100 Celsius."""
    return -100 <= temperature <= 100


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


if __name__ == "__main__":
    celsius = float(input("Enter temperature in Celsius: "))
    if valid_temperature(celsius):
        print(f"{celsius_to_fahrenheit(celsius):.2f}°F")
    else:
        print("The temperature is out of range.")
