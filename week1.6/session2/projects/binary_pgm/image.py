# Week 1.6, Session 2

"""
Classes for working with images.
"""

import copy


class ImageError(Exception):
    """
    Exception for problems that may occur when creating Image objects.
    """


class Image:
    """
    A greyscale image.
    """

    @classmethod
    def create(cls, width, height, value=0, maximum=255):
        """
        Creates an Image with the given dimensions.

        All pixels are initialized to 0 by default, but you can provide a
        different value as an argument after width and height.

        A maximum allowed value can be also be specified; if not provided,
        it defaults to 255.
        """
        image = Image()
        image.create_pixels(width, height, value, maximum)
        return image

    @classmethod
    def read(cls, filename):
        """
        Creates an Image from data in the specified PGM file.
        """
        image = Image()
        image.read_pgm(filename)
        return image

    def create_pixels(self, width, height, value=0, maximum=255):
        """
        Creates a new array of pixels, replacing any existing image data.

        All pixels are initialized to 0 by default, but you can provide a
        different value as an argument after width and height.

        A maximum allowed value can be also be specified; if not provided,
        it defaults to 255.
        """
        if width < 1:
            raise ImageError("width cannot be < 1")
        if height < 1:
            raise ImageError("height cannot be < 1")

        self.width = width
        self.height = height
        self.max_value = maximum
        self.pixels = [value] * (width * height)

    def read_pgm(self, filename):
        """Read either ASCII P2 or binary P5 PGM, including header comments."""
        def next_token(stream):
            """Read a PGM header token, ignoring comments and whitespace."""
            token = bytearray()
            while True:
                char = stream.read(1)
                if not char:
                    if token:
                        return bytes(token)
                    raise ImageError("Unexpected end of PGM header")
                if char == b"#":
                    stream.readline()
                    if token:
                        return bytes(token)
                    continue
                if char in b" \t\r\n":
                    if token:
                        return bytes(token)
                    continue
                token.extend(char)

        with open(filename, "rb") as source:
            magic = next_token(source)
            if magic not in (b"P2", b"P5"):
                raise ImageError("Only P2 and P5 PGM are supported")
            width = int(next_token(source))
            height = int(next_token(source))
            maximum = int(next_token(source))
            if width < 1 or height < 1 or not 1 <= maximum <= 65535:
                raise ImageError("Invalid PGM dimensions or maximum")
            if magic == b"P2":
                pixels = [int(next_token(source)) for _ in range(width * height)]
            else:
                bytes_per_pixel = 1 if maximum < 256 else 2
                raw = source.read(width * height * bytes_per_pixel)
                if len(raw) != width * height * bytes_per_pixel:
                    raise ImageError("Truncated P5 pixel data")
                if bytes_per_pixel == 1:
                    pixels = list(raw)
                else:
                    pixels = [int.from_bytes(raw[i:i + 2], "big")
                              for i in range(0, len(raw), 2)]
            if any(not 0 <= pixel <= maximum for pixel in pixels):
                raise ImageError("Pixel value out of range")
            self.width, self.height, self.max_value, self.pixels = (
                width, height, maximum, pixels)

    def write_pgm(self, filename, binary=False):
        """Save a P2 image, or a compact P5 binary PGM if requested."""
        if not binary:
            with open(filename, "wt", encoding="ascii") as out:
                self._write_header(out)
                self._write_pixels(out)
            return
        width = 1 if self.max_value < 256 else 2
        with open(filename, "wb") as out:
            out.write(f"P5\\n{self.width} {self.height}\\n{self.max_value}\\n".encode("ascii"))
            for pixel in self.pixels:
                out.write(int(pixel).to_bytes(width, "big"))

    def _parse_magic_number(self, imgfile):
        line = imgfile.readline().strip()
        if line != "P2":
            raise ImageError("unrecognized magic number")

    def _parse_dimensions(self, imgfile):
        line = imgfile.readline().strip()
        if line.startswith("#"):
            # Ignore comment and read another line
            line = imgfile.readline().strip()
        parts = line.split()
        self.width = int(parts[0])
        self.height = int(parts[1])

    def _parse_max_value(self, imgfile):
        line = imgfile.readline().strip()
        self.max_value = int(line)

    def _parse_pixels(self, imgfile):
        self.pixels = [int(value) for value in imgfile.read().split()]

        if len(self.pixels) != self.width * self.height:
            raise ImageError("number of pixels doesn't match image dimensions")

        if any(p < 0 or p > self.max_value for p in self.pixels):
            raise ImageError(f"pixel value outside allowed range (0 to {self.max_value})")

    def __getitem__(self, index):
        """
        Returns pixel value at the specified linear index.
        """
        return self.pixels[index]

    def __setitem__(self, index, value):
        """
        Sets pixel at the specified linear index to the specified value.
        """
        self.pixels[index] = value

    def get(self, row, col):
        """
        Returns pixel value at the specified row & column coordinates.
        """
        index = row * self.width + col
        return self.pixels[index]

    def set(self, row, col, value):
        """
        Sets pixel at the specified row & column coordinates to the given value.
        """
        index = row * self.width + col
        self.pixels[index] = value

    def copy(self):
        """
        Returns a new Image that is a copy of this Image.
        """
        return copy.deepcopy(self)

    def _write_header(self, imgfile):
        print("P2", file=imgfile)
        print(self.width, self.height, file=imgfile)
        print(self.max_value, file=imgfile)

    def _write_pixels(self, imgfile):
        for row in range(self.height):
            start = row * self.width
            for value in self.pixels[start:start + self.width]:
                print(f"{value:4d}", end="", file=imgfile)
            print(file=imgfile)
