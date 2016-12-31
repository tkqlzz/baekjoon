import collections


def bfs():
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    q = collections.deque()
    cache = set()
    arr[0][0] = 2
    res, q_cnt = 0, 1
    while q_cnt:
        res += 1
        q_cnt = 0
        set_cnt = set()
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 2:
                    q.append((i, j))
                    arr[i][j] = -1
                    q_cnt += 1
        q += cache
        cache = set()
        while q:
            y, x = q.popleft()
            for dy, dx in direct:
                cy = y + dy
                cx = x + dx
                if cy < 0 or cx < 0 or cy >= n or cx >= m:
                    continue
                if arr[cy][cx] == 0:
                    arr[cy][cx] = -1
                    q.append((cy, cx))
                elif arr[cy][cx] == 1:
                    if (cy, cx) in set_cnt:
                        arr[cy][cx] = 2
                    else:
                        set_cnt.add((cy, cx))
                        cache.add((y, x))

    print(res - 2)


n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

bfs()
