import math

m, n = map(int, input().split())

prime_list = [0, 0] + [1] * (n-1)

for i in range(2, int(math.sqrt(n))+1):
    if prime_list[i]:
        for j in range(i*i, n+1, i):
            prime_list[j] = 0

for i in range(2, n+1):
    if prime_list[i]:
        if m <= i <= n:
            print(i)
