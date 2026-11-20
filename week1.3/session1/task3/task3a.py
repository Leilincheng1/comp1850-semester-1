"""Print integers from 1 to 20 except multiples of three."""
i = 0

while True:
    print(i)
    i = i + 1
    if i > 3:
        break
# Add logic using continue so that multiples of 3 are not printed out
# Hint: we discused operators such as % and // in recent weeks

# Hint 2: there are several ways to do this - using truthy/falsey values is the least code
while i < 20:
    i += 1
    if i % 3 == 0:
        continue
    print(i)
