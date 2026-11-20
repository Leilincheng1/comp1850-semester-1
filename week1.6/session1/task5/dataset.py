# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.6, Session 1: Task 5
#
# from datetime import datetime
#
# from feed import QuakeFeed
# from quake import Quake
#
#
# class QuakeDatasetError(Exception):
#     """
#     An exception type for errors involving QuakeDataset.
#     """
#
#
# class QuakeDataset:
#     """
#     An earthquake dataset obtained from a USGS data feed.
#     """
#
#     def __init__(self, feed):
#         """
#         Creates an empty dataset, linked to a specific data feed.
#         """
#         if not isinstance(feed, QuakeFeed):
#             raise TypeError("feed must be specified as a QuakeFeed object")
#
#         self.feed = feed
#         self.data = []
#
#     def read_feed(self):
#         """
#         Refreshes this dataset with data from the linked feed.
#
#         The new data replaces any existing data.
#         """
        # Write code here to replace existing data with new earthquake data.
        # Use the value returned by the feed's reader() method as the
        # subject of a for loop.
#
        # Keep in mind that the items obtained by this for loop will be
        # dictionaries. You will need to extract the required values from
        # each dictionary and convert them into the required types before
        # creating a Quake object and storing it in the list.
#
#     def __len__(self):
#         """
#         Returns the size of this dataset.
#         """
        # Write code here that returns the number of quakes downloaded
#
#     def __str__(self):
#         """
#         Returns information on this dataset as a string.
#         """
        # Write code here to create and return a string representation
        # (Include number of quakes and details of the feed that was used)
#
#     def mean_depth(self):
#         """
#         Returns the mean depth of the quakes in this dataset.
#         """
#         if len(self.data) == 0:
#             raise QuakeDatasetError("dataset is empty")
#
#         total = sum(quake.depth for quake in self.data)
#         return total / len(self.data)
#
#     def mean_magnitude(self):
#         """
#         Returns the mean magnitude of the quakes in this dataset.
#         """
        # Write code here that computes the mean magnitude of all the
        # quakes currently in the dataset
#
#     def shallowest_quake(self):
#         """
#         Returns details of the shallowest quake in this dataset.
#         """
#         if len(self.data) == 0:
#             raise QuakeDatasetError("dataset is empty")
#
#         shallowest = self.data[0]
#         for quake in self.data[1:]:
#             if quake.depth < shallowest.depth:
#                 shallowest = quake
#         return shallowest
#
#     def strongest_quake(self):
#         """
#         Returns details of the strongest quake in this dataset.
#         """
        # Write code here that finds and returns the strongest quake
        # (i.e., the one with the largest magnitude)
# ============================================================================
# Completed solution
# ============================================================================
"""Retrieve and analyse earthquake events from a USGS feed."""
from datetime import datetime
from feed import QuakeFeed
from quake import Quake


class QuakeDatasetError(Exception):
    """Problem with an empty or invalid earthquake dataset."""


class QuakeDataset:
    """An earthquake dataset tied to a USGS CSV feed."""

    def __init__(self, feed):
        """Create an empty dataset associated with a QuakeFeed."""
        if not isinstance(feed, QuakeFeed):
            raise TypeError("feed must be specified as a QuakeFeed object")
        self.feed = feed
        self.data = []

    def read_feed(self):
        """Replace existing quake data with freshly parsed feed rows."""
        loaded = []
        for row in self.feed.reader():
            try:
                loaded.append(Quake(
                    when=datetime.fromisoformat(row["time"].replace("Z", "+00:00")),
                    longitude=float(row["longitude"]),
                    latitude=float(row["latitude"]),
                    depth=float(row["depth"]),
                    magnitude=float(row["mag"]),
                ))
            except (ValueError, TypeError, KeyError):
                continue  # Incomplete events cannot be represented as Quake.
        self.data = loaded

    def __len__(self):
        """Return the number of earthquakes."""
        return len(self.data)

    def __str__(self):
        """Identify the number of events and the feed."""
        return f"{len(self)} quakes, from {self.feed}"

    def _require_data(self):
        if not self.data:
            raise QuakeDatasetError("dataset is empty")

    def mean_depth(self):
        """Return the mean earthquake depth in kilometres."""
        self._require_data()
        return sum(quake.depth for quake in self.data) / len(self)

    def mean_magnitude(self):
        """Return the mean earthquake magnitude."""
        self._require_data()
        return sum(quake.magnitude for quake in self.data) / len(self)

    def shallowest_quake(self):
        """Return the event with the smallest depth."""
        self._require_data()
        return min(self.data, key=lambda quake: quake.depth)

    def strongest_quake(self):
        """Return the quake with the largest magnitude."""
        self._require_data()
        return max(self.data, key=lambda quake: quake.magnitude)

    def deepest_quake(self):
        """Return the quake with the greatest depth."""
        self._require_data()
        return max(self.data, key=lambda quake: quake.depth)

    def weakest_quake(self):
        """Return the quake with the smallest magnitude."""
        self._require_data()
        return min(self.data, key=lambda quake: quake.magnitude)

    def nearby_quakes(self, longitude, latitude, degrees):
        """Return quakes within a simple coordinate-degree radius."""
        self._require_data()
        return [quake for quake in self.data
                if ((quake.longitude - longitude) ** 2 +
                    (quake.latitude - latitude) ** 2) ** 0.5 <= degrees]

    def format_table(self):
        """Return a readable table of earthquake details."""
        self._require_data()
        lines = ["Date/time | Longitude | Latitude | Depth (km) | Magnitude"]
        for quake in self.data:
            lines.append(f"{quake.when.isoformat()} | {quake.longitude:.2f} | "
                         f"{quake.latitude:.2f} | {quake.depth:.2f} | "
                         f"{quake.magnitude:.1f}")
        return "\n".join(lines)
