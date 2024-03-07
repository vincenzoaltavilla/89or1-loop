def sumSquaredDigits(n):
    sum = 0
    for digit in n:
        digit = int(digit)
        sum = sum + (digit * digit)
    return sum


for n in range(1, 1001):
    n = str(n)
    sum = sumSquaredDigits(n)
    i = 0

    while sum != 89 and sum != 1:
        i = i + 1
        sum = sumSquaredDigits(str(sum))

    print(n, 'goes to', sum, 'through', i, 'steps')
