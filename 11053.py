n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
for i in range(n):
    maxDp = 1
    for j in reversed(range(i)):
        if arr[i] > arr[j] and dp[j] >= maxDp:
            maxDp = dp[j] + 1
    dp[i] = maxDp

print(max(dp))

"""
7
10 40 15 20 30 60 80
"""