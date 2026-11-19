"""Read an image, blur it and write it to an output PGM file."""
import sys
from image import Image
from filters import blur


def main():
    """Run image blur from the two specified CLI file names."""
    if len(sys.argv) != 3:
        sys.exit("Usage: python blur.py original.pgm blurred.pgm")
    try:
        source = Image.read(sys.argv[1])
        blur(source).write_pgm(sys.argv[2])
        print(f"Wrote blurred image to {sys.argv[2]}")
    except (OSError, ValueError) as error:
        sys.exit(f"Error: {error}")


if __name__ == "__main__":
    main()
