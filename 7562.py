def bfs(y, x):
    direct = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]

    q = [[y, x]]
    while q:
        y, x = q.pop(0)
        if (y, x) == (f_y, f_x):
            break
        for d in direct:
            dy = y + d[0]
            dx = x + d[1]
            if dy < 0 or dx < 0 or dy >= n or dx >= n:
                continue
            if arr[dy][dx] == 0:
                arr[dy][dx] = arr[y][x] + 1
                q.append([dy, dx])
    print(arr[f_y][f_x])

for t in range(int(input())):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    s_y, s_x = map(int, input().split())
    f_y, f_x = map(int, input().split())
    bfs(s_y, s_x)