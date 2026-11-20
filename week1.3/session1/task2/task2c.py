"""Read characters one at a time until the file reaches EOF."""
from pathlib import Path

with (Path(__file__).parent / "file_data.txt").open(encoding="utf-8") as file:
    while True:
        char = file.read(1)
        # The read returns an empty string only once end-of-file is reached.
        if not char:
            break
        print(char)
