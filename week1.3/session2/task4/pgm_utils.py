"""Helpers for the Week 1.3 text-based (P2) PGM exercises."""
from pathlib import Path


def read_pgm(path):
    """Return width, height, max gray and rows; retain actual row lengths."""
    lines = []
    with Path(path).open(encoding="ascii") as source:
        for line in source:
            clean = line.split("#", 1)[0].strip()
            if clean:
                lines.append(clean)
    if not lines or lines[0] != "P2":
        raise ValueError("Unsupported PGM format (expected P2)")
    width, height = map(int, lines[1].split())
    maximum = int(lines[2])
    rows = [list(map(int, line.split())) for line in lines[3:]]
    return width, height, maximum, rows


def validate_pgm(width, height, maximum, rows):
    """Return a task-specified verdict for pixel and dimension problems."""
    if any(len(row) != width for row in rows):
        return "Invalid width"
    if len(rows) != height:
        return "Invalid height"
    if maximum <= 0 or any(not 0 <= value <= maximum for row in rows for value in row):
        return "Invalid pixel values"
    return "Valid image"


def write_pgm(path, width, height, maximum, rows):
    """Save rows as a plain-text P2 image."""
    with Path(path).open("w", encoding="ascii") as destination:
        destination.write(f"P2\n{width} {height}\n{maximum}\n")
        for row in rows:
            destination.write(" ".join(map(str, row)) + "\n")
