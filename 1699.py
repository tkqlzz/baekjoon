import math

n = int(input())
dp = [0, 1] + [0] * (n-1)
arr = []

sqrtn = int(math.sqrt(n))
for i in range(1, sqrtn+1):
    arr.append(i*i)

for i in range(1, n+1):
    for j in arr:
        if j > i:
            break
        if dp[i] > dp[i-j] + 1 or dp[i] == 0:
            dp[i] = dp[i-j] + 1

print(dp[n])