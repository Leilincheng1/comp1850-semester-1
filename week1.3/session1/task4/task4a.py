"""Print the running sum of even squares through 20."""
total = 0
for k in range(2, 21, 2):
    total += k ** 2
    print(f"After {k}: {total}")
