def bfs():
    minVisit = 98765321
    for i in range(n):
        visit = [0] * n
        for j in range(n):
            if i == j:
                continue
            if arr[i][j]:
                q = [j]
                visit[j] = 1
                while q:
                    x = q.pop(0)
                    for k in range(n):
                        if i == k:
                            continue
                        if arr[i][k]:
                            continue
                        if arr[x][k] and (visit[k] > visit[x] + 1 or visit[k] == 0):
                            q.append(k)
                            visit[k] = visit[x] + 1
        sumVisit = sum(visit)
        if minVisit > sumVisit:
            minVisit = sumVisit
            result = i
    print(result+1)

n, m = map(int, input().split())
arr = [[0] * n for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1

bfs()