n = int(input())
stair = [0] * (n+1)
dp = [0] * (n+1)
for i in range(1, n+1):
    stair[i] = int(input())

for i in range(1, 4):
    if i != 3:
        dp[i] = dp[i-1] + stair[i]
    else:
        dp[i] = max(stair[i] + dp[i-2], stair[i] + stair[i-1])

for i in range(4, n+1):
    dp[i] = max(stair[i] + dp[i-2], stair[i] + stair[i-1] + dp[i-3])

print(dp)
print(dp[n])
