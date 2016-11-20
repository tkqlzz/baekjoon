def bfs():
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                q = [[i, j]]
                arr[i][j] = 1
                cnt = 1
                while q:
                    cur = q.pop(0)
                    for di in direct:
                        dy = cur[0] + di[0]
                        dx = cur[1] + di[1]
                        if dx < 0 or dy < 0 or dx >= n or dy >= m:
                            continue
                        if arr[dy][dx] == 0:
                            arr[dy][dx] = 1
                            q.append([dy, dx])
                            cnt += 1
                result.append(cnt)
    result.sort()


m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
result = []
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1
bfs()
print(len(result))
for i in result:
    print(i, end=" ")