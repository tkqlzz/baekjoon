import collections


def bfs():
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    q = collections.deque()

    arr[0][0] = 2

    cnt, q_cnt = 0, 1
    while q_cnt:
        cnt += 1
        before, q_cnt = q_cnt, 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 2:
                    q.append([i, j])
                    arr[i][j] = -1
                    q_cnt += 1
        while q:
            y, x = q.popleft()
            for dy, dx in direct:
                cy = y + dy
                cx = x + dx
                if cy < 0 or cx < 0 or cy >= n or cx >= m:
                    continue
                if arr[cy][cx] == 0:
                    arr[cy][cx] = -1
                    q.append([cy, cx])
                elif arr[cy][cx] == 1:
                    arr[cy][cx] = 2
    print(cnt - 2)
    print(before)


n, m = map(int, input().split())
arr = []
cache = [[0] * m for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int, input().split())))

bfs()
