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
