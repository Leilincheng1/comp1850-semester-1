# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.6, Session 1: Task 5
#
# Write a program here that uses the QuakeFeed and QuakeDataset
# classes to download earthquake data from a USGS data feed,
# analyze it and display the results
#
# See README.md for full details of what is required and what
# program output should look like
# ============================================================================
# Completed solution
# ============================================================================
"""Read and summarise a current earthquake feed."""
from feed import QuakeFeed
from dataset import QuakeDataset, QuakeDatasetError


def main():
    """Prompt for a feed, retrieve events and display useful statistics."""
    level = input("Significance (all, 1.0, 2.5, 4.5, significant) [4.5]: ").strip() or "4.5"
    period = input("Period (hour, day, week, month) [week]: ").strip() or "week"
    try:
        feed = QuakeFeed(level, period)
        dataset = QuakeDataset(feed)
        dataset.read_feed()
        print(dataset)
        print(f"Mean depth = {dataset.mean_depth():.2f} km")
        print(f"Mean magnitude = {dataset.mean_magnitude():.2f}")
        strongest = dataset.strongest_quake()
        print(f"Strongest quake occurred at {strongest.when:%H:%M:%S} "
              f"on {strongest.when:%Y-%m-%d}")
        print(f"at {strongest.longitude}° longitude, {strongest.latitude}° latitude")
        print(f"The depth was {strongest.depth} km")
        print(f"The magnitude was {strongest.magnitude}")
    except (ValueError, OSError, QuakeDatasetError) as error:
        print(f"Unable to analyse the earthquake feed: {error}")


if __name__ == "__main__":
    main()
