# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.3, Session 1: Task 6b
#
# values = [1,4,2,6,3,7]
#
# print(values)
#
# newval = []
# for i in values:
#     if i % 2 == 0:
#         newval.append(2 * i)
#     else:
#         newval.append(i)
#
# print(newval)
#
# write the list comprehension equivalent to the `for` loop
#
# ============================================================================
# Completed solution
# ============================================================================
"""Double even integers using loops and comprehensions."""
values = [1, 4, 2, 6, 3, 7]
newval = []
for value in values:
    if value % 2 == 0:
        newval.append(2 * value)
    else:
        newval.append(value)
newval_comp = [2 * value if value % 2 == 0 else value for value in values]
print(newval)

# write the list comprehension equivalent to the `for` loop

values = [1,4,2,6,3,7]

newval = [2* i if i % 2 ==0 else i for i in values]
print(newval)
print(newval_comp)
assert newval == newval_comp
