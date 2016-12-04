import collections


def bfs():
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    q = collections.deque()
    q.append((0, 0))

    while q:
        y, x = q.popleft()
        for dy, dx in direct:
            ny = y + dy
            nx = x + dx
            if ny < 0 or nx < 0 or ny >= m or nx >= n:
                continue
            else:
                q.append((ny, nx))


m, n = map(int, input().split())
board = []

for i in range(m):
    board.append(input())

bfs()
