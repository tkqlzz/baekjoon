def dfs(x, y):
    global cnt
    if y == (m-1) and x == (n-1):
        return 1
    if visit[y][x]:
        return visit[y][x]

    for d in direct:
        dy = y + d[0]
        dx = x + d[1]
        if dy < 0 or dx < 0 or dy >= m or dx >= n:
            continue
        if arr[dy][dx] < arr[y][x]:
            visit[y][x] += dfs(dx, dy)
    return visit[y][x]

direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
cnt = 0
m, n = map(int, input().split())
arr = [[]]*m
visit = [[0] * n for _ in range(m)]

for i in range(m):
    arr[i] = list(map(int, input().split()))

print(dfs(0, 0))