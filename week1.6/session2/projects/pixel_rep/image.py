"""Grayscale Image using a list of lists instead of a flat pixel list."""
import copy


class ImageError(Exception):
    """Image format or pixel validation failed."""


class Image:
    """A P2 grayscale image with pixels organized by row."""

    @classmethod
    def create(cls, width, height, value=0, maximum=255):
        """Build an image with all pixels initialized to a value."""
        image = cls()
        image.create_pixels(width, height, value, maximum)
        return image

    @classmethod
    def read(cls, filename):
        """Read a grayscale PGM image."""
        image = cls()
        image.read_pgm(filename)
        return image

    def create_pixels(self, width, height, value=0, maximum=255):
        """Replace image pixels with a rectangular list of lists."""
        if width < 1 or height < 1 or maximum < 1 or not 0 <= value <= maximum:
            raise ImageError("Invalid image dimensions or pixel values")
        self.width, self.height, self.max_value = width, height, maximum
        self.pixels = [[value for col in range(width)] for row in range(height)]

    def read_pgm(self, filename):
        """Parse P2 pixels into row lists, supporting header comments."""
        with open(filename, encoding="ascii") as source:
            tokens = []
            for line in source:
                tokens.extend(line.split("#", 1)[0].split())
        if len(tokens) < 4 or tokens[0] != "P2":
            raise ImageError("Expected P2 PGM")
        width, height, maximum = map(int, tokens[1:4])
        values = list(map(int, tokens[4:]))
        if (width < 1 or height < 1 or maximum < 1 or
                len(values) != width * height or
                any(not 0 <= value <= maximum for value in values)):
            raise ImageError("Invalid image data")
        self.width, self.height, self.max_value = width, height, maximum
        self.pixels = [values[index:index + width]
                       for index in range(0, len(values), width)]

    def get(self, row, col):
        """Return a pixel using its row and column."""
        return self.pixels[row][col]

    def set(self, row, col, value):
        """Change one pixel."""
        if type(value) is not int or not 0 <= value <= self.max_value:
            raise ImageError("Invalid pixel")
        self.pixels[row][col] = value

    def copy(self):
        """Return an independent copy of this image."""
        return copy.deepcopy(self)

    def write_pgm(self, filename):
        """Write the image in P2 plain-text PGM format."""
        with open(filename, "w", encoding="ascii") as output:
            output.write(f"P2\\n{self.width} {self.height}\\n{self.max_value}\\n")
            for row in self.pixels:
                output.write(" ".join(map(str, row)) + "\\n")


if __name__ == "__main__":
    img = Image.create(3, 2)
    img.set(1, 2, 125)
    assert img.get(1, 2) == 125
    assert img.copy().get(1, 2) == 125
