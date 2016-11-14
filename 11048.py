n, m = map(int, input().split())
matrix = []
dp = [[0] * m for _ in range(n)]
direct = [[0, 1], [1, 0], [1, 1]]

for i in range(n):
    matrix.append(list(map(int, input().split())))

dp[0][0] = matrix[0][0]

for i in range(n):
    for j in range(m):
        for x, y in direct:
            dx = i + x
            dy = j + y

            if dx >= n or dy >= m:
                continue

            if dp[dx][dy] < dp[i][j] + matrix[dx][dy]:
                dp[dx][dy] = dp[i][j] + matrix[dx][dy]


print(dp[n-1][m-1])
