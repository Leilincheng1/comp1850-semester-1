"""Print a descending sequence recursively and iteratively."""


def countdown(n):
    """Print integers from n to zero using recursion."""
    if n < 0:
        return
    print(n)
    countdown(n - 1)


def countdown_loop(n):
    """Print the same countdown using a for loop."""
    for number in range(n, -1, -1):
        print(number)


if __name__ == "__main__":
    countdown(30)
    countdown(5)
    countdown_loop(5)
