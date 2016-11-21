# 타일 채우기
n = int(input())
dp = [1, 0, 3] + [0] * (n-2)
for i in range(4, n+1, 2):
    dp[i] = dp[i-2] * 3
    for j in range(4, i+1, 2):
        dp[i] += dp[i-j] * 2

print(dp[n])
"""
1 3 11 41 153 571 2131
0 3 9 33 123              // dp[n] = dp[n-2] * 3
0 0 2 6+2 22+6+2          // dp[n] += dp[n-j] * 2 .........
"""