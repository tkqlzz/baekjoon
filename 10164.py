def bfs(sy, sx, ey, ex):
    direct = [[0, 1], [1, 0]]

    q = [(sy, sx)]
    matrix[sy][sx] = 1

    while q:
        y, x = q.pop(0)
        for dy, dx in direct:
            cy = dy + y
            cx = dx + x
            if cy >= ey + 1 or cx >= ex + 1:
                continue
            if matrix[cy][cx]:
                matrix[cy][cx] += matrix[y][x]
            else:
                matrix[cy][cx] += matrix[y][x]
                q.append((cy, cx))
    return matrix[ey][ex]


n, m, k = map(int, input().split())
matrix = [[0] * m for j in range(n)]

if k == 0:
    ky, kx = 0, 0
else:
    k -= 1
    ky, kx = k // m, k % m

print(bfs(0, 0, ky, kx) * bfs(ky, kx, n - 1, m - 1))