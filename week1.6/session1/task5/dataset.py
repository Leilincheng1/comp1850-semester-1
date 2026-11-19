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
