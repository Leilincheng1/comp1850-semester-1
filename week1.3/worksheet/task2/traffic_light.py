"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())

state = "red"
remaining = states[state]

print(f"Time {systime:03} State {state}")

for systime in range(1, maxtime + 1):
    remaining -= 1

    if remaining == 0:
        if state == "red":
            state = "red_amber"
        elif state == "red_amber":
            state = "green"
        elif state == "green":
            state = "amber"
        elif state == "amber":
            state = "red"

        remaining = states[state]

    print(f"Time {systime:03} State {state}")