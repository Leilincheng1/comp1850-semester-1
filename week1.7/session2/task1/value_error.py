"""Iterate over a dictionary's (key, value) pairs."""

user_profile = {"username": "alice99", "role": "admin"}
for key, value in user_profile.items():
    print(f"{key} : {value}")
