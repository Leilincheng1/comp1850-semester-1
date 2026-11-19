"""Use match statements for a basic ATM and arithmetic calculator."""


def atm(balance, choice, amount=0):
    """Return a new balance and transaction description."""
    match choice:
        case 1:
            return balance, f"Balance: £{balance:.2f}"
        case 2 if amount > 0:
            return balance + amount, f"Deposited £{amount:.2f}"
        case 3 if 0 < amount <= balance:
            return balance - amount, f"Withdrawn £{amount:.2f}"
        case 2 | 3:
            return balance, "Invalid transaction amount"
        case _:
            return balance, "Invalid option"


def calculate(a, op, b):
    """Return the arithmetic result using match-case."""
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return "Cannot divide by zero" if b == 0 else a / b
        case _:
            return "Unknown operator"


def main():
    """Run simple demonstrations of both match-based programs."""
    balance, message = atm(1000, 2, 50)
    print(message, balance)
    expression = input("Enter a calculation (e.g. 2 + 5): ")
    try:
        left, operator, right = expression.split()
        print(calculate(float(left), operator, float(right)))
    except ValueError:
        print("Enter NUMBER OPERATOR NUMBER, separated by spaces.")


if __name__ == "__main__":
    main()
