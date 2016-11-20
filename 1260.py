def dfs(s):
    print(s+1, end=" ")
    for i in range(e):
        if arr[s][i] == 1 and visit[i] == 0:
            visit[i] = 1
            dfs(i)


def bfs(s):
    q = [s]
    while q:
        cur = q.pop(0)
        print(cur+1, end=" ")
        for i in range(e):
            if arr[cur][i] == 1 and visit2[i] == 0:
                visit2[i] = 1
                q.append(i)


e, v, start = map(int, input().split())
arr = [[0] * e for i in range(e)]
visit = [0] * e
visit[start-1] = 1
visit2 = [0] * e
visit2[start-1] = 1

for i in range(v):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1


dfs(start-1)
print()
bfs(start-1)