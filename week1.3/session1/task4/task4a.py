# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.3, Session 1: Task 4a
#
# sum = 0
#
# for k in range(1,10):
#     sum = sum + k ** 2
#
# print(sum)
#
#
# modify the code to sum the squares of even numbers up to and including 20
#
# modify the code to print the sum at each iteration
# ============================================================================
# Completed solution
# ============================================================================
"""Print the running sum of even squares through 20."""
total = 0
for k in range(2, 21, 2):
    total += k ** 2
    print(f"After {k}: {total}")
