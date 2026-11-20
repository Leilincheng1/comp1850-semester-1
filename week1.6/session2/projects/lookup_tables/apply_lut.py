"""Apply a specified lookup table to a PGM image."""
import sys
from image import Image
from lookup import InvertTable, SquareRootTable


def main():
    """Read and transform a PGM image with a pixel LUT."""
    if len(sys.argv) != 4 or sys.argv[3] not in ("invert", "sqrt"):
        sys.exit("Usage: python apply_lut.py input.pgm output.pgm invert|sqrt")
    image = Image.read(sys.argv[1])
    table = (InvertTable(image.max_value) if sys.argv[3] == "invert"
             else SquareRootTable(image.max_value))
    transformed = table.apply(image)
    transformed.write_pgm(sys.argv[2])
    print(f"Wrote {sys.argv[2]}")


if __name__ == "__main__":
    main()
