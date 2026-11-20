"""Apply a discount based on membership and student status."""
cost = int(input("Amount spent: "))
is_member = input("Are you a member? (y/n): ").strip().lower()
is_student = input("Are you a student? (y/n): ").strip().lower()
if is_member == "y" and is_student == "y":
    final_cost = cost * 0.70
elif is_member == "y":
    final_cost = cost * 0.75
elif is_student == "y":
    final_cost = cost * 0.85
else:
    final_cost = cost
print(f"Final amount including discount: {final_cost:.2f}")
