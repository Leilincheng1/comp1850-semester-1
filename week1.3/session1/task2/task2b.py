"""Echo user input until 'quit' is entered."""
print("This program will repeat everything you type.")
print("To exit the program type quit")
while True:
    user_input = input("Say something: ")
    if user_input == "quit":
        break
    print(f"You said: {user_input}")
