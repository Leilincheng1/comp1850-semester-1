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
