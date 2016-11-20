def bfs():
    while q:
        cur = q.pop(0)
        if cur == y:
            print(visit[cur])
            break
        push(cur - 1, cur)
        push(cur + 1, cur)
        push(cur * 2, cur)


def push(t, cur):
    if maxSize > t >= 0 == visit[t]:
        visit[t] = visit[cur] + 1
        q.append(t)


x, y = map(int, input().split())
maxSize = 100001
visit = [0] * maxSize
q = [x]
bfs()