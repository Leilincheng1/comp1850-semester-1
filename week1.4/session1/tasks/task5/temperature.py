# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 4, Session 1: 
#
# To convert a temperature from Celsius to Fahrenheit. 
# There are two main tasks involved:
#   (1) validating the temperature 
#   (2) converting Celsius to Fahrenheit.
#
# These are now defined in a separate function.
#
# Given the two functions and the following code to get the temperature
# from a user, complete the rest of the program to use these functions to
# print the temperature in Fahrenheit if the temperature from the user
# is within the range, otherwise print "The temperature is out of range."
#
#
#
# def valid_temperature(temperature):
#     if temperature >= -100 and temperature <= 100:
#         return True
#     else:
#         return False
#
#
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit
#
#
# test the functions
#
# celsius = float(input("Enter temperature in Celsius: "))
#
# Complete the rest of the code here
# ============================================================================
# Completed solution
# ============================================================================
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
