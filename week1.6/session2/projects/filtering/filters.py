"""Apply a simple 3x3 mean blur with a zero-valued border."""
from image import Image


def blur(img):
    """Return a new Image containing an integer-rounded 3x3 neighbourhood mean."""
    result = Image.create(img.width, img.height, maximum=img.max_value)
    for row in range(1, img.height - 1):
        for col in range(1, img.width - 1):
            total = sum(img.get(row + dr, col + dc)
                        for dr in (-1, 0, 1) for dc in (-1, 0, 1))
            result.set(row, col, round(total / 9))
    return result
