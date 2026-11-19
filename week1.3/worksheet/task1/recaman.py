# Worksheet 1.3: Task 1

length = int(input("Length of sequence: "))
sequence = []

if length > 0:
    sequence.append(0)
    seen = {0}
    for step in range(1, length):
        previous = sequence[-1]
        candidate = previous - step
        if candidate <= 0 or candidate in seen:
            candidate = previous + step
        sequence.append(candidate)
        seen.add(candidate)

for value in sequence:
    print(value)
