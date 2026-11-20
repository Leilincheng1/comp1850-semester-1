"""Compare linear pixel access and row/column pixel access timing."""
from time import perf_counter
from image import Image


def benchmark(width=500, height=500, repeats=5):
    """Return elapsed seconds for two ways of reading image pixels."""
    image = Image.create(width, height, value=42)
    start = perf_counter()
    for _ in range(repeats):
        total_linear = sum(image[index] for index in range(width * height))
    linear_time = perf_counter() - start

    start = perf_counter()
    for _ in range(repeats):
        total_grid = sum(image.get(row, col)
                         for row in range(height) for col in range(width))
    grid_time = perf_counter() - start
    assert total_linear == total_grid
    return linear_time, grid_time


if __name__ == "__main__":
    linear, grid = benchmark()
    print(f"Linear indexing: {linear:.4f}s")
    print(f"Row/column access: {grid:.4f}s")
