import collections


def bfs():
    q = collections.deque([[0, 0]])
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    cnt = 0
    while q:
        y, x = q.popleft()
        cnt += 1

        for dy, dx in direct:
            cy, cx = y + dy, x + dx

            if cy < 0 or cx < 0 or cy >= n or cx >= m:
                continue

            if arr[cy][cx] == '1':
                if dp[cy][cx] > dp[y][x] + 1:
                    dp[cy][cx] = dp[y][x] + 1
                    q.append([cy, cx])
            elif arr[cy][cx] == '0':
                if dp[cy][cx] > dp[y][x]:
                    dp[cy][cx] = dp[y][x]
                    q.append([cy, cx])

m, n = map(int, input().split())
arr = []
dp = [[987654321] * m for _ in range(n)]

for i in range(n):
    arr.append(input())
dp[0][0] = int(arr[0][0])

bfs()
print(dp[n-1][m-1])