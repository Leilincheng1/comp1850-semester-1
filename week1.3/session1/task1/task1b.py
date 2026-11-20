# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# Week 1.3, Session 1: Task 1b
#
# fruit = ['apple','pear','banana','orange']
#
# loop through the list
# while fruit:
# 	print(fruit.pop())
#
#
# Why does this work?
#
# What features of Python does it rely on?
# ============================================================================
# Completed solution
# ============================================================================
"""Pop items from a list until it is empty."""
fruit = ["apple", "pear", "banana", "orange"]
# First iteration: orange removed, leaving apple/pear/banana.
# Fourth iteration: apple removed, leaving [].
# After the loop: []. Empty lists are false in Boolean contexts.
while fruit:
    print(fruit.pop())
