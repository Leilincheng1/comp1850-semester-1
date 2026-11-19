"""Collect and alphabetically sort characters from a course name."""
course = "computer science"
characters = []
for character in course:
    print(character)
    characters.append(character)
characters.sort()
print(characters)
