import sys
from collections import deque
read = sys.stdin.readline


def bfs(graph, visit):
    q = deque()
    q.append((x, 0))
    while q:
        now, s = q.popleft()
        for i, w in graph[now]:
            if s + w < visit[i]:
                visit[i] = s + w
                q.append((i, s+w))

n, m, x = map(int, input().split())
visit = [987654321] * (n+1)
r_visit = [987654321] * (n+1)
visit[x] = 0
r_visit[x] = 0

graph = [[] for i in range(n+1)]
r_graph = [[] for i in range(n+1)]
for i in range(m):
    u, v, w = map(int, read().split())
    graph[u].append((v, w))
    r_graph[v].append((u, w))

bfs(graph, visit)
bfs(r_graph, r_visit)

max_num = 0
for i in range(1, n+1):
    max_num = max(max_num, visit[i] + r_visit[i])

print(max_num)