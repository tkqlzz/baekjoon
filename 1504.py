import collections
import sys
read = sys.stdin.readline


def bfs(start, end):
    cache = [987654321] * (n + 1)
    cache[start] = 0
    q = collections.deque()
    q.append((start, 0))
    while q:
        now, x = q.popleft()
        for v, w in graphs[now]:
            if (x + w) < cache[v]:
                cache[v] = x + w
                q.append((v, x + w))
    return cache[end]


n, e = map(int, read().split())

graphs = [[] for _ in range(n + 1)]
for _ in range(e):
    v1, v2, weight = map(int, read().split())
    graphs[v1].append((v2, weight))
    graphs[v2].append((v1, weight))

a, b = map(int, read().split())

res = min((bfs(1, a) + bfs(a, b) + bfs(b, n)), (bfs(1, b) + bfs(b, a) + bfs(a, n)))
if res >= 987654321:
    print(-1)
else:
    print(res)
