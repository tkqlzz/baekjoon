def getMax(i, m):
    if i == n-1:
        return arr[i]
    if i >= n:
        return -1000000
    if m == 1:
        return getMax(i+2, 2) + arr[i]
    if m == 2:
        return max(getMax(i+1, 1) + arr[i], getMax(i+2, 1) + arr[i])

n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = int(input())

dp = [0] * n
dp[0] = arr[0]

m = 2
i = 1
while i < n-1:
    if m == 1:
        dp[i] = dp[i-1] + arr[i]
        m = 2
    elif m == 2:
        if dp[i-1] + arr[i] > dp[i-1] + arr[i+1]:
            dp[i] = dp[i-1] + arr[i]
            dp[i + 1] = dp[i]
            m = 1
            i += 1
        else:
            dp[i] = dp[i - 1] + arr[i + 1]
            dp[i + 1] = dp[i]
            m = 2
            i += 1
    i += 1

print(dp)
print(max(getMax(0, 1), getMax(0, 2)))