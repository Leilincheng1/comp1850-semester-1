# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.2, Session 1: Task 6
#
# from pprint import pprint
#
# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
#
# Pretty-print the data structure
#
# Display details of one album recorded by a specific artist
# ============================================================================
# Completed solution
# ============================================================================
"""Store sample albums by artist, including their release years."""
from pprint import pprint

music = {
    "The Beatles": [{"album": "Abbey Road", "year": 1969},
                    {"album": "Revolver", "year": 1966}],
    "Daft Punk": [{"album": "Discovery", "year": 2001},
                   {"album": "Random Access Memories", "year": 2013}],
}
pprint(music)
print(music["Daft Punk"][0]["album"])
print(f"Total albums: {sum(len(albums) for albums in music.values())}")
