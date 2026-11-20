"""Try the five Boolean comparison expressions from Task 1."""
expressions = [( "7 > 4", 7 > 4), ("9 < 1", 9 < 1),
               ("8 >= 3", 8 >= 3), ('"hello" == "Hello"', "hello" == "Hello"),
               ('"a" > "e"', "a" > "e")]
for expression, result in expressions:
    print(f"{expression} => {result}")
