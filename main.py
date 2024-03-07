
for n in range(1000):
    n = n+1
    tot = 0
    n = str(n)

    for digit in n:
        digit = int(digit)
        tot = tot + (digit * digit)

    i = 0
    while tot != 89 and tot != 1:
        i = i+1
        sum2 = str(tot)
        tot = 0
        for digit2 in sum2:
            digit2 = int(digit2)
            tot = tot + (digit2 * digit2)

    print(n, '-', tot, '-', i)