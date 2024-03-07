def sumSquaredDigits(n):
    sum = 0
    for digit in n:
        digit = int(digit)
        sum = sum + (digit * digit)
    return sum

NUMBERS = 1000000
max = 0

for n in range(1, NUMBERS):
    n = str(n)
    sum = sumSquaredDigits(n)
    i = 0

    while sum != 89 and sum != 1:
        i = i + 1
        if i > max:
            max = i

        sum = sumSquaredDigits(str(sum))

    print(n, 'goes to', sum, 'through', i, 'steps')

print('The maximum number of steps for the first', NUMBERS, 'numbers is', max)