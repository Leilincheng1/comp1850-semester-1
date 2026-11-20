# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.7, Session 2: Task 1 - ValueError
#
# Run this program and observe what happens
#
# user_profile = {"username": "alice99", "role": "admin"}
#
# for key, value in user_profile:
# 	print(f"{key} : {value}")
# ============================================================================
# Completed solution
# ============================================================================
"""Iterate over a dictionary's (key, value) pairs."""

user_profile = {"username": "alice99", "role": "admin"}
for key, value in user_profile.items():
    print(f"{key} : {value}")
