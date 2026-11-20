"""Double a number until the newly computed value exceeds 200."""
k = 2
while True:
    k = 2 * k 
    if k > 200:
        break
while k <= 200:
    k *= 2
    print(k)
