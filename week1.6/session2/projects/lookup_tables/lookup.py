"""Build and apply pixel lookup tables to greyscale Image objects."""
from math import sqrt
from image import Image


class LookupTable:
    """A grayscale mapping from [0, maximum] to that same range."""

    def __init__(self, mapping):
        """Validate and store integer mapped values."""
        if not mapping or any(type(value) is not int or
                              not 0 <= value < len(mapping) for value in mapping):
            raise ValueError("Lookup entries must be integers inside the gray range")
        self.mapping = list(mapping)

    def display(self):
        """Print each input to output pixel mapping."""
        for original, mapped in enumerate(self.mapping):
            print(f"{original} -> {mapped}")

    def apply(self, image):
        """Return a new image after applying this LUT."""
        result = image.copy()
        self.apply_in_place(result)
        return result

    def apply_in_place(self, image):
        """Apply the LUT to the image, mutating each pixel."""
        if image.max_value >= len(self.mapping):
            raise ValueError("LUT does not cover image gray range")
        for index in range(image.width * image.height):
            image[index] = self.mapping[image[index]]


class InvertTable(LookupTable):
    """Invert grayscale brightness."""

    def __init__(self, maximum=255):
        super().__init__([maximum - value for value in range(maximum + 1)])


class SquareRootTable(LookupTable):
    """Enhance dark regions via a nonlinear square-root transform."""

    def __init__(self, maximum=255):
        super().__init__([round(sqrt(value / maximum) * maximum)
                          for value in range(maximum + 1)])
