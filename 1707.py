import collections
import sys
read = sys.stdin.readline


def bfs(i):
    q = collections.deque()
    q.append(i)
    cache[i] = 0

    while q:
        cur = q.popleft()
        x = (cache[cur] + 1) % 2
        for v in graph[cur]:
            if cache[v] == -1:
                cache[v] = x
                q.append(v)
            else:
                if cache[v] != x:
                    return False
    return True


for t_case in range(int(read())):
    v, e = map(int, read().split())
    graph = [[] for _ in range(v + 1)]
    cache = [-1] * (v+1)

    for i in range(e):
        v1, v2 = map(int, read().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    for i in range(1, v+1):
        if cache[i] == -1:
            if not bfs(i):
                print("NO")
                break
        if i == v:
            print("YES")
