# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Worksheet 1.2: Task 1 Solution
# ============================================================================
# Completed solution
# ============================================================================
# Worksheet 1.2: Task 1 Solution

import sys

try:
    grade = int(input("Enter an integer grade in the range 0 to 100: "))
except ValueError:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if grade < 0 or grade > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if grade >= 70:
    print(f"{grade} is a Distinction")
elif grade >= 40:
    print(f"{grade} is a Pass")
else:
    print(f"{grade} is a Fail")
