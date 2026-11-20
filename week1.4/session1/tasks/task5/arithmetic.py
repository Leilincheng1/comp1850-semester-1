# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 4, Session 1: 
#
# There are 5 functions defined below, one for each arithmetic operation
# and one for getting user inputs. Please inspect the code and then
# complete the code for case 1 to case 4.
#
#
# def addition(num1, num2):
#     return num1 + num2
#
#
# def subtraction(num1, num2):
#     return num1 - num2
#
#
# def multiplication(num1, num2):
#     return num1 * num2
#
#
# def division(num1, num2):
#     if num2 == 0:
#         return "Error: cannot divide by zero"
#     else:
#         return num1 / num2
#
#
# def run_program():
#
    # Ask user for two numbers
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#
    # Ask user for the desired operation
#     print("Select an operation:")
#     print("1. Addition (+)")
#     print("2. Subtraction (-)")
#     print("3. Multiplication (*)")
#     print("4. Division (/)")
#     operation = int(input("Enter your choice (1-4): "))
#
#     match operation:
#         case 1:
#             result = None    # complete this line of code
#             print(f"The result of addition is: {result}")
#         case 2:
#             result = None    # complete this line of code
#             print(f"The result of subtraction is: {result}")
#         case 3:
#             result = None   # complete this line of code
#             print(f"The result of multiplication is: {result}")
#         case 4:
#             result = None    # complete this line of code
#             print(f"The result of division is: {result}")
#         case _:
#             print("Undefined operation")
#
#
# run_program()
#
#
# In the function run_program, they are more than one tasks involved:
#   (1) getting user input for numbers
#   (2) ask user for desired operation
#   (3) match operation.
#
#    If you are to split each task into a separate function, how would you
#   name the function for each of these tasks?
# ============================================================================
# Completed solution
# ============================================================================
"""Perform arithmetic using separate input and operation functions."""


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return "Error: cannot divide by zero" if b == 0 else a / b


def get_numbers():
    """Prompt for two floating-point operands."""
    return float(input("Enter the first number: ")), float(input("Enter the second number: "))


def select_operation():
    """Ask the user which arithmetic operation they want."""
    print("1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)\n4. Division (/)")
    return int(input("Enter your choice (1-4): "))


def run_program():
    """Read operands and print the requested calculation."""
    num1, num2 = get_numbers()
    operation = select_operation()
    match operation:
        case 1:
            print(f"The result of addition is: {addition(num1, num2)}")
        case 2:
            print(f"The result of subtraction is: {subtraction(num1, num2)}")
        case 3:
            print(f"The result of multiplication is: {multiplication(num1, num2)}")
        case 4:
            print(f"The result of division is: {division(num1, num2)}")
        case _:
            print("Undefined operation")


if __name__ == "__main__":
    run_program()
