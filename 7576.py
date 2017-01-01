import collections


def bfs():
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    q = collections.deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                q.append([i, j])

    while q:
        y, x = q.popleft()
        for d in direct:
            dy = y + d[0]
            dx = x + d[1]
            if dy < 0 or dx < 0 or dy >= n or dx >= m:
                continue
            if arr[dy][dx] == 0:
                arr[dy][dx] = arr[y][x] + 1
                q.append([dy, dx])

    max_num = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                print(-1)
                return
            if max_num < arr[i][j]:
                max_num = arr[i][j]
    print(max_num - 1)


m, n = map(int, input().split())
arr = [[]] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))

bfs()
