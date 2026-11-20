# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.2, Session 2: Task 4
# Simple Number Comparer
#
# Prompt the user to enter the numbers
#
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
#
# Use an if statement to compare the two numbers
#
# if XXX: 
#     print("The first number is bigger.")
# elif XXX:  
#     print("The second number is bigger.")
# else:
#     print("Both numbers are Equal.")
# ============================================================================
# Completed solution
# ============================================================================
"""Compare two real numbers."""
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print("The first number is bigger.")
elif num2 > num1:
    print("The second number is bigger.")
else:
    print("Both numbers are Equal.")
