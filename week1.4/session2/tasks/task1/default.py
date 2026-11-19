"""Demonstrate default and explicit name arguments."""


def greeting(name="Student"):
    """Greet the supplied name or use a neutral default."""
    print(f"Good morning {name}")


if __name__ == "__main__":
    greeting()
    greeting("Alex")
