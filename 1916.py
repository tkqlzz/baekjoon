import collections
import sys


def bfs():
    visit = [987654321] * (n + 1)
    visit[start] = 0

    q = collections.deque()
    q.append((start, 0))

    while q:
        now, s = q.popleft()
        for i, w in graph[now]:
            if s + w < visit[i]:
                visit[i] = s + w
                q.append((i, s+w))
    print(visit[end])


read = sys.stdin.readline
n = int(read())
m = int(read())

graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y, w = map(int, read().split())
    graph[x].append((y, w))

start, end = map(int, read().split())
bfs()
