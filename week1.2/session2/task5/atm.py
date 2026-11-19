"""Demonstrate simple ATM balance, deposit and withdrawal operations."""
balance = 1000.0
print("Welcome to the ATM!")
print("Select an option: ")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
option = int(input("Enter your option (1-3): "))
if option == 1:
    print(f"Your current balance is: £{balance:.2f}")
elif option == 2:
    deposit_amount = float(input("Enter the amount to deposit: "))
    if deposit_amount <= 0:
        print("Deposit must be positive.")
    else:
        balance += deposit_amount
        print(f"You have deposited £{deposit_amount:.2f}")
        print(f"Your new balance is £{balance:.2f}")
elif option == 3:
    withdraw_amount = float(input("Enter the amount to withdraw: "))
    if 0 < withdraw_amount <= balance:
        balance -= withdraw_amount
        print(f"You have withdrawn £{withdraw_amount:.2f}")
        print(f"Your new balance is £{balance:.2f}")
    else:
        print("Insufficient funds or invalid withdrawal amount.")
else:
    print("Invalid option. Please try again.")
