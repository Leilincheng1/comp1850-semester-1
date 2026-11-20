"""Compare a list comprehension with an equivalent for loop."""
animals = ["dog", "cat", "hamster", "goldfish"]
not_fish = [animal for animal in animals if animal != "goldfish"]
not_fish_2 = []
for animal in animals:
    if animal != "goldfish":
        not_fish_2.append(animal)
print(not_fish)


# write the equivalent for loop to create the not_fish list from animals
# print your result to verify it is the same

animals = ['dog','cat','hamster','goldfish']
not_fish = []
for i in animals:
    if i != 'goldfish'
    not_fish.append(i)
    
print(not_fish_2)
assert not_fish == not_fish_2

"""Compare a list comprehension with an equivalent for loop."""

animals = ["dog", "cat", "hamster", "goldfish"]

not_fish = [animal for animal in animals if animal != "goldfish"]

not_fish_2 = []
for animal in animals:
    if animal != "goldfish":
        not_fish_2.append(animal)

print(not_fish)
print(not_fish_2)

assert not_fish == not_fish_2
