import collections
import sys
read = sys.stdin.readline


def bfs():
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    q = collections.deque()

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if maps[i][j][k] == 1:
                    q.append((i, j, k))

    while q:
        z, y, x = q.popleft()
        for dy, dx in direct:
            cy = y + dy
            cx = x + dx
            if cy < 0 or cx < 0 or cy >= n or cx >= m:
                continue
            if maps[z][cy][cx] == 0:
                maps[z][cy][cx] = maps[z][y][x] + 1
                q.append([z, cy, cx])
        if 0 < z:
            if maps[z - 1][y][x] == 0:
                maps[z - 1][y][x] = maps[z][y][x] + 1
                q.append([z - 1, y, x])
        if z < (h - 1):
            if maps[z + 1][y][x] == 0:
                maps[z + 1][y][x] = maps[z][y][x] + 1
                q.append([z + 1, y, x])

    res = 0
    for i in maps:
        for j in i:
            for k in j:
                if k == 0:
                    print(-1)
                    return
                res = max(res, k)
    print(res-1)


m, n, h = map(int, read().split())
maps = []

for _ in range(h):
    arr = []
    for __ in range(n):
        arr.append(list(map(int, read().split())))
    maps.append(arr)

bfs()
