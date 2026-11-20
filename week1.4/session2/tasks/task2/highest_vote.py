# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 4, Session 2: Task 2
#
# def most_frequent_string(votes):
#     """
#     This function identifies the string that appears most frequently
#     (highest count) in the votes argument and returns it along with the count
#     of its occurrences. It assumes there is a single most frequent string
#     (i.e., no ties for the highest count)
#
#     Args:
#         votes (list): A list of strings representng votes,
#         e.g. ['apples', 'bananas', 'grapes', 'tomatoes']
#
#     Returns:
#         - tuple: (str, int) where str is the string with the highest count,
#         and int is the count of its occurences
#         - None, None: if votes is empty.
#     """
#
    # Your task is to complete the body of the function based on the details in the docstring.
    # Hint 1: You can complete this task with for loops or comprehensions 
    # Hint 2: Think about the properties of the various collection-types
#
#
# fruit = ['date', 'apple', 'cherry', 'date', 'apple', 'apple', 'elderberry',
#          'date', 'elderberry', 'elderberry', 'date', 'banana']
# names = ['Jesy', 'Leigh-Anne', 'Perrie', 'Leigh-Anne', 'Jade',
#          'Leigh-Anne', 'Perrie', 'Leigh-Anne', 'Jesy', 'Jade',
#          'Leigh-Anne', 'Leigh-Anne', 'Leigh-Anne', 'Leigh-Anne',
#          'Leigh-Anne', 'Jade', 'Jesy', 'Jade', 'Perrie', 'Jade',
#          'Jade', 'Jesy', 'Perrie', 'Perrie', 'Jade', 'Leigh-Anne',
#          'Jesy', 'Jesy', 'Perrie', 'Jesy']
#
#
# Check if correct output is produced
# print(most_frequent_string(fruit))          # ('date', 4)
# print(most_frequent_string(names))     # ('Leigh-Anne', 10)
# print(most_frequent_string([]))             # (None, None)
#
# If completed, you could update the function to return all items that tie for the
# highest count in a list, e.g  (['apples', 'bananas'], 9). If there is no
# tie, return a single string and a value as usual, e.g ('apples, 9).
# ============================================================================
# Completed solution
# ============================================================================
"""Find the most frequent string, including tied leaders."""
from collections import Counter


def most_frequent_string(votes):
    """Return (winning string, count) or (list of tied winners, count)."""
    if not votes:
        return None, None
    counts = Counter(votes)
    maximum = max(counts.values())
    winners = [name for name, count in counts.items() if count == maximum]
    return (winners[0] if len(winners) == 1 else winners), maximum


if __name__ == "__main__":
    fruit = ["date", "apple", "cherry", "date", "apple", "apple",
             "elderberry", "date", "elderberry", "elderberry", "date", "banana"]
    names = ["Jesy", "Leigh-Anne", "Perrie", "Leigh-Anne", "Jade",
             "Leigh-Anne", "Perrie", "Leigh-Anne", "Jesy", "Jade",
             "Leigh-Anne", "Leigh-Anne", "Leigh-Anne", "Leigh-Anne",
             "Leigh-Anne", "Jade", "Jesy", "Jade", "Perrie", "Jade",
             "Jade", "Jesy", "Perrie", "Perrie", "Jade", "Leigh-Anne",
             "Jesy", "Jesy", "Perrie", "Jesy"]
    print(most_frequent_string(fruit))
    print(most_frequent_string(names))
    print(most_frequent_string([]))
