import math


def factor_simple(n):
    arr = []
    if n >= 10:
        sqrtn = int(math.sqrt(n)) + 1
    else:
        sqrtn = n
    for div in range(2, sqrtn):
        while n % div == 0:
            n //= div
            arr.append(div)
    if n > 1:
        arr.append(n)
    return arr


n = int(input())
for i in factor_simple(n):
    print(i)
