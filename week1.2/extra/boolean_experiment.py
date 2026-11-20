"""Explain why isinstance(False, int) is True in Python."""
answer = False
print(isinstance(answer, int))  # True: bool is a subclass of int.
print(type(answer) is int)  # False: its exact type is bool.
print(isinstance(answer, bool))  # True.
