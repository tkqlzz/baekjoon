n = int(input())
m = int(input())
floyd = [[987654321] * n for row in range(n)]

for i in range(n):
    floyd[i][i] = 0

for i in range(m):
    u, v, w = map(int, input().split())
    floyd[u-1][v-1] = min(floyd[u-1][v-1], w)

for k in range(n):
    for i in range(n):
        for j in range(n):
            floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])

for i in range(n):
    for j in range(n):
        print(floyd[i][j], end=" ")
    print()