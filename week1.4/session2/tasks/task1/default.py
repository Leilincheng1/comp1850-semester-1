# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 4, Session 2: Task 1
#
# def greeting(name='John'):
    # Your task is change the default name to your name and observe the output
#     print(f'Good morning {name}')
#
#
# Check if correct output is produced
# greeting()
#
# write a second test by passing a name to the function
# ============================================================================
# Completed solution
# ============================================================================
"""Demonstrate default and explicit name arguments."""


def greeting(name="Student"):
    """Greet the supplied name or use a neutral default."""
    print(f"Good morning {name}")


if __name__ == "__main__":
    greeting()
    greeting("Alex")
