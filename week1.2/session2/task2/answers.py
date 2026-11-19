"""Try the six logical expressions from Task 2."""
expressions = [
    ("not (3 > 1)", not (3 > 1)),
    ("(4 > 2) and (6 > 8)", (4 > 2) and (6 > 8)),
    ("(5 == 5) or (2 > 10)", (5 == 5) or (2 > 10)),
    ("not (10 > 5 or 3 != 3)", not (10 > 5 or 3 != 3)),
    ("5 < 10 < 15", 5 < 10 < 15),
    ("3 <= 3 < 10 and (10 == 10 or 5 > 8)", 3 <= 3 < 10 and (10 == 10 or 5 > 8)),
]
for expression, result in expressions:
    print(f"{expression} => {result}")
