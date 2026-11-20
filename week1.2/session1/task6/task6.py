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
