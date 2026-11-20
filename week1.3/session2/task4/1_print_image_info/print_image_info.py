"""Display dimensions and grayscale range for a P2 image."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pgm_utils import read_pgm

image = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "images" / "plus.pgm"
try:
    width, height, maximum, _ = read_pgm(image)
    print(f"Dimensions: {width} x {height} pixels")
    print(f"Max Gray Value: {maximum}")
except (OSError, ValueError, IndexError) as error:
    print(f"Cannot read PGM image: {error}")
