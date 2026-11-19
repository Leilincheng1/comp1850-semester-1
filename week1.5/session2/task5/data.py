"""A numeric dataset loaded from a text file."""


class Dataset:
    """A numeric dataset containing numbers read from a file."""

    def __init__(self, filename=None):
        """Create an empty dataset, or load a data file."""
        self.data = []
        if filename:
            self.load_data(filename)

    def load_data(self, filename):
        """Replace the existing data with one float per line from a file."""
        with open(filename, encoding="utf-8") as source:
            new_data = [float(line.strip()) for line in source if line.strip()]
        self.data = new_data

    def __len__(self):
        """Return the number of observations."""
        return len(self.data)

    def __getitem__(self, index):
        """Return an observation at an index."""
        return self.data[index]

    def mean(self):
        """Return the arithmetic mean, or None for empty datasets."""
        return sum(self.data) / len(self.data) if self.data else None

    def median(self):
        """Return the median without altering the original order."""
        if not self.data:
            return None
        values = sorted(self.data)
        middle = len(values) // 2
        if len(values) % 2:
            return values[middle]
        return (values[middle - 1] + values[middle]) / 2
