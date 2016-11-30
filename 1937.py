import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline


def dfs(y, x):
    cache[y][x] += 1
    for dy, dx in direct:
        cy = dy + y
        cx = dx + x
        if cy < 0 or cx < 0 or cy >= n or cx >= n:
            continue
        if matrix[y][x] < matrix[cy][cx]:
            if cache[cy][cx]:
                cache[y][x] = max(cache[y][x], cache[cy][cx] + 1)
            else:
                cache[y][x] = max(cache[y][x], dfs(cy, cx) + 1)
    return cache[y][x]


direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]

n = int(read())

matrix = []
for i in range(n):
    matrix.append(list(map(int, read().split())))
cache = [[0] * n for _ in range(n)]

k = 0
for i in range(n):
    for j in range(n):
        if cache[i][j] == 0:
            k = max(dfs(i, j), k)


print(k)