"""Invert every pixel of a valid P2 grayscale image."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pgm_utils import read_pgm, validate_pgm, write_pgm

source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "images" / "plus.pgm"
destination = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_name("inverted.pgm")
try:
    width, height, maximum, rows = read_pgm(source)
    if validate_pgm(width, height, maximum, rows) != "Valid image":
        raise ValueError("Source image is invalid")
    inverted = [[maximum - pixel for pixel in row] for row in rows]
    write_pgm(destination, width, height, maximum, inverted)
    print(f"Wrote inverted image to {destination}")
except (OSError, ValueError, IndexError) as error:
    print(f"Cannot invert image: {error}")
