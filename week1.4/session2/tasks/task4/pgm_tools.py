# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
#
# PGM functions that we write
#
# def readPGM( filename ):
#     ''' 
#     Read a named PGM file and store the data in a tuple.
#     Input: filename string
#     Output: tuple of PGM image data
#     '''
#
#     with open(filename,"r") as f:    # read in the file
#         data = f.readlines()
#         
#     data = [line.strip().split() for line in data[1:]] # clean the space-separated data, skip the first line
#           
#     width = int(data[0][0]) # store the data - compare to the text in the file
#     height = int(data[0][1])
#     max_gray = int(data[1][0])
#     pixels = [[int(data[2+i][j]) for j in range(width)] for i in range(height)] # nested list comprehension for pixel array
#     
#     return width,height,max_gray,pixels   # tuple of PGM data
#     
# def writePGM( filename, image ):
#     '''
#     Write a PGM file to disk
#     Input: filename string, image tuple data
#     Output: None
#     '''
#     width,height,max_gray,pixels = image  # unpack the tuple
#
    # open a file for writing
    # write the data in PGM format
    # don't forget the PGM code "P2"
#
#     return
#
# def invertPGM( image ):
#     '''
#     Invert an image, ie. pixel value = 255 - pixel value
#     Input: image data
#     Output: inverted image data
#     '''
#     width,height,max_gray,pixels = image  # unpack the tuple
#
    # your code
    # create a new pixel array of inverted data 
#     inverted = []  # you can use a similar nested comprehension to the readPGM() function
#     
#     return width,height,max_gray,inverted
#
# code to test the PGM functions
#
# image = readPGM("images/feep.pgm")
#
# print(f"Image with width {image[0]} and height {image[1]}")
# print(f"{image[3]}")
#
# write further code to test your own functions
# ============================================================================
# Completed solution
# ============================================================================
"""Read, write, invert, rotate and threshold text PGM (P2) images."""
from pathlib import Path


def readPGM(filename):
    """Return (width, height, max_gray, pixel rows) for a text PGM."""
    tokens = []
    for line in Path(filename).read_text(encoding="ascii").splitlines():
        tokens.extend(line.split("#", 1)[0].split())
    if not tokens or tokens[0] != "P2":
        raise ValueError("Expected a P2 PGM")
    width, height, max_gray = map(int, tokens[1:4])
    values = list(map(int, tokens[4:]))
    if width <= 0 or height <= 0 or len(values) != width * height:
        raise ValueError("Invalid PGM dimensions")
    if any(not 0 <= value <= max_gray for value in values):
        raise ValueError("Invalid grayscale pixel")
    pixels = [values[i:i + width] for i in range(0, len(values), width)]
    return width, height, max_gray, pixels


def writePGM(filename, image):
    """Write a tuple of image dimensions and pixels to a P2 file."""
    width, height, max_gray, pixels = image
    if len(pixels) != height or any(len(row) != width for row in pixels):
        raise ValueError("Pixel array does not match dimensions")
    with open(filename, "w", encoding="ascii") as output:
        output.write(f"P2\n{width} {height}\n{max_gray}\n")
        for row in pixels:
            output.write(" ".join(map(str, row)) + "\n")


def invertPGM(image):
    """Return a new image with inverted gray values."""
    width, height, maximum, pixels = image
    return width, height, maximum, [
        [maximum - pixel for pixel in row] for row in pixels
    ]


def rotate90PGM(image):
    """Rotate an image clockwise through ninety degrees."""
    width, height, maximum, pixels = image
    rotated = [[pixels[height - 1 - y][x] for y in range(height)]
               for x in range(width)]
    return height, width, maximum, rotated


def thresholdPGM(image, threshold):
    """Replace pixels with black or maximum gray based on a threshold."""
    width, height, maximum, pixels = image
    changed = [[maximum if pixel >= threshold else 0 for pixel in row]
               for row in pixels]
    return width, height, maximum, changed


if __name__ == "__main__":
    source = Path(__file__).parent / "images" / "feep.pgm"
    original = readPGM(source)
    print(f"Image with width {original[0]} and height {original[1]}")
    writePGM(Path(__file__).parent / "feep_copy.pgm", original)
    writePGM(Path(__file__).parent / "feep_inverted.pgm", invertPGM(original))
    writePGM(Path(__file__).parent / "feep_rotated.pgm", rotate90PGM(original))
    writePGM(Path(__file__).parent / "feep_threshold.pgm", thresholdPGM(original, 8))
