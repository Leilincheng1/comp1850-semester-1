"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Lei LinCheng
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

user_input = input ("Enter your monthly savings amount:")
try:    
    monthly = int(user_input.strip())
    yearly = monthly * 12
    total = yearly * 1.008
    print(f"You will save ￡{yearly} every year.")
    print(f"With interest, you will save £{total:.2f} per year.")
except ValueError:
        print("Invalid amount")

