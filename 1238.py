import sys
read = sys.stdin.readline

n, m, x = map(int, read().split())
x -= 1
floyd = [[987654321] * n for row in range(n)]

for i in range(n):
    floyd[i][i] = 0

for i in range(m):
    u, v, w = map(int, read().split())
    floyd[u-1][v-1] = min(floyd[u-1][v-1], w)

for k in range(n):
    for i in range(n):
        for j in range(n):
            floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])

max_num = 0
for i in range(n):
    max_num = max(floyd[i][x] + floyd[x][i], max_num)
print(max_num)
print(floyd)