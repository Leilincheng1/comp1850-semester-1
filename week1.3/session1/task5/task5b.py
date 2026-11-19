"""Iterate over dictionary entries, keys and values."""
rivers = {"London": "Thames", "Leeds": "Aire", "Liverpool": "Mersey", "York": "Ouse"}
for city, river in rivers.items():
    print(city, river)
for city in rivers.keys():
    print(city)
for river in rivers.values():
    print(river)
