import collections


def bfs():
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    q = collections.deque()
    q.append((0, 0))

    while q:
        y, x = q.popleft()
        for dy, dx in direct:
            cy = y + dy
            cx = x + dx
            if 0 <= cy < n and 0 <= cx < m:
                q.append((cy, cx))


n, m = map(int, input().split())
board = []

for i in range(n):
    board.append(list(map(int, input())))

bfs()
