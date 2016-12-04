import collections


def bfs():
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    max_cnt = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'L':
                visit = [[0] * n for _ in range(m)]
                q = collections.deque()
                q.append((i, j))

                while q:
                    y, x = q.popleft()
                    for dy, dx in direct:
                        ny = y + dy
                        nx = x + dx
                        if ny < 0 or nx < 0 or ny >= m or nx >= n:
                            continue
                        if board[ny][nx] == 'L' and visit[ny][nx] == 0:
                            visit[ny][nx] = 1 + visit[y][x]
                            q.append((ny, nx))
                max_cnt = max(max_cnt, visit[y][x])
    print(max_cnt)


m, n = map(int, input().split())
board = []

for i in range(m):
    board.append(input())

bfs()
