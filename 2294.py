n, k = map(int, input().split())
arr = [0] * n
dp = [987654321] * (k+1)
dp[0] = 0
for i in range(n):
    arr[i] = int(input())

for coin in arr:
    for j in range(k+1):
        if j >= coin:
            dp[j] = min(dp[j], dp[j-coin] + 1)

if dp[k] == 987654321:
    print(-1)
else:
    print(dp[k])