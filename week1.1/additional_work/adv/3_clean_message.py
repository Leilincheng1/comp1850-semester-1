"""Clean a message using string methods and compare its length."""

original = input("Type a message to tidy: ")
# Strip outer whitespace, normalize repeated spaces, and title-case words.
cleaned_message = " ".join(original.strip().split()).title()
print(f"Original message: {original}")
print(f"Cleaned message: {cleaned_message}")
print(f"Original length: {len(original)}")
print(f"Cleaned length: {len(cleaned_message)}")
