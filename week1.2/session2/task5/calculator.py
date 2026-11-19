"""Choose an arithmetic operation for two integers."""
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
print("Select an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
operation = int(input("Enter your choice (1-4): "))
if operation == 1:
    print(f"The result of addition is: {num1 + num2}")
elif operation == 2:
    print(f"The result of subtraction is: {num1 - num2}")
elif operation == 3:
    print(f"The result of multiplication is: {num1 * num2}")
elif operation == 4:
    if num2 != 0:
        print(f"The result of division is: {num1 / num2}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation selected.")
