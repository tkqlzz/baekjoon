n = int(input())
dp = [0, 0]

for i in range(2, n+1):
    dp.append(dp[i - 1] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i - 1] + 1, dp[i // 3] + 1)

print(dp[n])