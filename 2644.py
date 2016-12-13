import collections


def bfs(a, b):

    q = collections.deque()
    q.append(a)

    while q:
        x = q.popleft()
        if x == b:
            print(visit[x])
            exit()
        for y in graph[x]:
            if visit[y] == 0:
                visit[y] = 1 + visit[x]
                q.append(y)
    print(-1)

n = int(input())
graph = [[] for i in range(n+1)]
visit = [0] * (n+1)
a, b = map(int, input().split())
for i in range(int(input())):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

bfs(a, b)
