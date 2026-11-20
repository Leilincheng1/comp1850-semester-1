"""Iterate over dictionary entries, keys and values."""
rivers = {"London": "Thames", "Leeds": "Aire", "Liverpool": "Mersey", "York": "Ouse"}
for city, river in rivers.items():
    print(city, river)
for city in rivers.keys():
    print(city)
for river in rivers.values():
    print(river)


for c in rivers.keys():
    print(c)

for r in rivers.values():
    print(r)