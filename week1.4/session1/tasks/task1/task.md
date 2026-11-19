# `input()` function

`input(prompt='')` reads one line from standard input and **returns a string** (without the trailing newline). Its optional `prompt` argument is a string displayed to the user before the input is read. The function never automatically converts the response into a number: use `int()` or `float()` if needed.

Example program:

```python
name = input("What is your name? ")
age = int(input("How old are you? "))
print(f"Hello {name}! Next year you will be {age + 1}.")
```

For example, entering `Ava` and `19` displays `Hello Ava! Next year you will be 20.`
