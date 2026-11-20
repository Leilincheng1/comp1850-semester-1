# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.3, Session 2: Validate image
#
# Open a pgm image
# You could handle file errors with try/except
#
# Read the file content
#
# Store the width, the height, and the maximum gray value
#
# For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive
#
# Check if the widths and heights are the same as specified
#
# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value
# ============================================================================
# Completed solution
# ============================================================================
"""Validate declared dimensions and pixel ranges in a P2 image."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pgm_utils import read_pgm, validate_pgm

image = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "images" / "plus.pgm"
try:
    print(validate_pgm(*read_pgm(image)))
except (OSError, ValueError, IndexError) as error:
    print(f"Invalid image: {error}")
