# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Worksheet 1.3: Task 1
#
# L = int(input("Length of sequence: ")) # this should be your only input
#
#
# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
#
#
# You may wish to use further output for testing purposes while you develop your code
#
# [print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure
#
# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence
# ============================================================================
# Completed solution
# ============================================================================
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
