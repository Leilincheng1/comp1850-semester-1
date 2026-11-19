"""Read, write and edit ASCII greyscale (P2) and colour (P3) images."""
import copy


class ImageError(Exception):
    """An image has invalid data or dimensions."""


class Image:
    """Common features for grayscale and RGB images."""

    MAGIC = None

    def __init__(self):
        """Create an image object before pixels have been assigned."""
        self.width = 0
        self.height = 0
        self.max_value = 255
        self.pixels = []

    @classmethod
    def create(cls, width, height, value=None, maximum=255):
        """Create a rectangular image filled with the given value."""
        result = cls()
        result.create_pixels(width, height, value, maximum)
        return result

    @classmethod
    def read(cls, filename):
        """Read an image of this class from disk."""
        result = cls()
        result.read_image(filename)
        return result

    def create_pixels(self, width, height, value=None, maximum=255):
        """Initialize width * height pixels."""
        if width < 1 or height < 1 or maximum < 1:
            raise ImageError("Invalid dimensions or maximum value")
        self.width, self.height, self.max_value = width, height, maximum
        pixel = self.default_pixel() if value is None else value
        self.validate_pixel(pixel)
        self.pixels = [pixel] * (width * height)

    def default_pixel(self):
        """Return the default value of one pixel (subclass responsibility)."""
        raise NotImplementedError

    def validate_pixel(self, value):
        """Raise ImageError if the pixel is invalid."""
        raise NotImplementedError

    def __getitem__(self, index):
        """Return the pixel at a linear index."""
        return self.pixels[index]

    def __setitem__(self, index, value):
        """Store one validated pixel at a linear index."""
        self.validate_pixel(value)
        self.pixels[index] = value

    def get(self, row, col):
        """Return a pixel using row/column coordinates."""
        return self.pixels[row * self.width + col]

    def set(self, row, col, value):
        """Set a pixel using row/column coordinates."""
        self.validate_pixel(value)
        self.pixels[row * self.width + col] = value

    def copy(self):
        """Return an independent copy of this image."""
        return copy.deepcopy(self)

    def parse_pixels(self, values):
        """Construct pixels from text tokens."""
        raise NotImplementedError

    def pixel_tokens(self, pixel):
        """Return serializable components of a pixel."""
        raise NotImplementedError

    def read_image(self, filename):
        """Read an ASCII P2 or P3 file, skipping PPM header comments."""
        with open(filename, "r", encoding="ascii") as source:
            tokens = []
            for line in source:
                tokens.extend(line.split("#", 1)[0].split())
        if len(tokens) < 4 or tokens[0] != self.MAGIC:
            raise ImageError(f"Expected {self.MAGIC} image")
        width, height, maximum = map(int, tokens[1:4])
        if width < 1 or height < 1 or maximum < 1:
            raise ImageError("Invalid header")
        self.width, self.height, self.max_value = width, height, maximum
        self.pixels = self.parse_pixels(list(map(int, tokens[4:])))
        if len(self.pixels) != width * height:
            raise ImageError("Incorrect number of pixels")
        for pixel in self.pixels:
            self.validate_pixel(pixel)

    def write_image(self, filename):
        """Write an ASCII P2 or P3 image."""
        with open(filename, "w", encoding="ascii") as output:
            output.write(f"{self.MAGIC}\\n{self.width} {self.height}\\n{self.max_value}\\n")
            for row in range(self.height):
                pixels = self.pixels[row * self.width:(row + 1) * self.width]
                pieces = [str(component) for pixel in pixels
                          for component in self.pixel_tokens(pixel)]
                output.write(" ".join(pieces) + "\\n")

    def write_pgm(self, filename):
        """Compatibility alias for writing the image."""
        self.write_image(filename)


class GreyImage(Image):
    """A greyscale image with integer pixel values."""

    MAGIC = "P2"

    def default_pixel(self):
        return 0

    def validate_pixel(self, value):
        if type(value) is not int or not 0 <= value <= self.max_value:
            raise ImageError("Invalid grey pixel")

    def parse_pixels(self, values):
        return values

    def pixel_tokens(self, pixel):
        return (pixel,)


class ColourImage(Image):
    """An RGB colour image with tuples of three integer components."""

    MAGIC = "P3"

    def default_pixel(self):
        return (0, 0, 0)

    def validate_pixel(self, value):
        if (not isinstance(value, tuple) or len(value) != 3 or
                any(type(component) is not int or
                    not 0 <= component <= self.max_value for component in value)):
            raise ImageError("Invalid RGB pixel")

    def parse_pixels(self, values):
        if len(values) % 3:
            raise ImageError("Incomplete RGB triplet")
        return [tuple(values[i:i + 3]) for i in range(0, len(values), 3)]

    def pixel_tokens(self, pixel):
        return pixel


if __name__ == "__main__":
    grey = GreyImage.create(2, 2, maximum=255)
    grey.set(0, 1, 180)
    grey.write_image("test_grey.pgm")
    assert GreyImage.read("test_grey.pgm").get(0, 1) == 180
    colour = ColourImage.create(2, 2, maximum=255)
    colour.set(0, 1, (255, 0, 0))
    colour.write_image("test_colour.ppm")
    assert ColourImage.read("test_colour.ppm").get(0, 1) == (255, 0, 0)
