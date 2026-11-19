"""Multiply two integers and report invalid input with the required message."""

try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
except ValueError:
    print("That is not a number")
else:
    print(number1 * number2)
