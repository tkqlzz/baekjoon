import collections


def bfs():
    q = collections.deque()
    q.append((s, 0))
    while q:
        now, cnt = q.popleft()
        if now == g:
            print(cnt)
            return
        for i in [u, -d]:
            next = now + i
            if next < 1 or next > f:
                continue
            if visit[next] == 0:
                q.append((next, cnt + 1))
                visit[next] = 1
    print('use the stairs')
    return


f, s, g, u, d = map(int, input().split())
visit = [0] * (f + 1)
bfs()