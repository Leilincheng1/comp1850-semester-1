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
