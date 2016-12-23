import collections


def bfs():
    visit = [0] * (n+1)
    q = collections.deque()
    q.append((0, 0))
    while q:
        now, cnt = q.popleft()
        if now == n-1:
            print(cnt)
            return
        for i in range(1, arr[now]+1):
            next = now + i
            if next >= n:
                continue
            if visit[next] == 0:
                q.append((next, cnt + 1))
                visit[next] = 1
    print(-1)
    return


n = int(input())
arr = list(map(int, input().split()))

bfs()