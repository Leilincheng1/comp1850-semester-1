# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.2, Session 1: Task 5
#
# rivers = {
#     "London": "Thames",
#     "Leeds": "Aire",
#     "Liverpool": "Mersey"
# }
#
# print(rivers)
#
# Add two new entries to the rivers database
#
# Display all the keys
#
# Display all the values
#
# Display all the key:value pairs, as tuples
#
# Delete an entry from the rivers database
# ============================================================================
# Completed solution
# ============================================================================
"""Create, inspect and update a simple river database."""
rivers = {"London": "Thames", "Leeds": "Aire", "Liverpool": "Mersey"}
print(rivers)
rivers["York"] = "Ouse"
rivers["Newcastle"] = "Tyne"
print(rivers)
print(rivers.keys())
print(rivers.values())
print(rivers.items())
del rivers["Liverpool"]
print(rivers)

# Extension: associate a city with several rivers using a list.
multiple_rivers = {"Leeds": ["Aire", "Wharfe"], "London": ["Thames", "Lea"]}
print(multiple_rivers)
