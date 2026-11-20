"""Alternative grayscale image implementation using array('B') pixel storage."""
from array import array
import copy


class ImageError(Exception):
    """Invalid image data or dimensions."""


class Image:
    """A P2 image whose 8-bit pixels are stored in an array."""

    @classmethod
    def create(cls, width, height, value=0, maximum=255):
        """Create a new image with an initial grayscale pixel value."""
        image = cls()
        image.create_pixels(width, height, value, maximum)
        return image

    @classmethod
    def read(cls, filename):
        """Read pixels from a text PGM image."""
        image = cls()
        image.read_pgm(filename)
        return image

    def create_pixels(self, width, height, value=0, maximum=255):
        """Allocate width*height bytes for pixels."""
        if width < 1 or height < 1 or not 1 <= maximum <= 255 or not 0 <= value <= maximum:
            raise ImageError("Invalid image dimensions or value")
        self.width, self.height, self.max_value = width, height, maximum
        self.pixels = array("B", [value] * (width * height))

    def read_pgm(self, filename):
        """Read P2 image pixels as unsigned bytes."""
        with open(filename, encoding="ascii") as source:
            tokens = []
            for line in source:
                tokens.extend(line.split("#", 1)[0].split())
        if not tokens or tokens[0] != "P2":
            raise ImageError("Expected P2 PGM")
        width, height, maximum = map(int, tokens[1:4])
        if width < 1 or height < 1 or not 1 <= maximum <= 255:
            raise ImageError("Invalid header")
        values = list(map(int, tokens[4:]))
        if len(values) != width * height or any(not 0 <= value <= maximum for value in values):
            raise ImageError("Invalid pixel array")
        self.width, self.height, self.max_value = width, height, maximum
        self.pixels = array("B", values)

    def __getitem__(self, index):
        """Return a pixel at a linear index."""
        return self.pixels[index]

    def __setitem__(self, index, value):
        """Update a pixel at a linear index."""
        if type(value) is not int or not 0 <= value <= self.max_value:
            raise ImageError("Pixel out of range")
        self.pixels[index] = value

    def get(self, row, col):
        """Get a pixel using two-dimensional coordinates."""
        return self.pixels[row * self.width + col]

    def set(self, row, col, value):
        """Change a pixel using two-dimensional coordinates."""
        self[row * self.width + col] = value

    def copy(self):
        """Create a deep copy."""
        return copy.deepcopy(self)

    def write_pgm(self, filename):
        """Write a plain-text P2 image."""
        with open(filename, "w", encoding="ascii") as destination:
            destination.write(f"P2\n{self.width} {self.height}\n{self.max_value}\n")
            for i in range(0, len(self.pixels), self.width):
                destination.write(" ".join(str(value) for value in
                                           self.pixels[i:i + self.width]) + "\n")


if __name__ == "__main__":
    image = Image.create(3, 2)
    image.set(1, 2, 125)
    assert image.get(1, 2) == 125
    assert image.copy().get(1, 2) == 125
