import collections


def bfs():
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    q = collections.deque()
    q.append((0, 0, board[0][0]))
    max_size = 1

    while q:
        y, x, data = q.popleft() # 0 0 C / 0 1 CA / 1 1 CAD
        for dy, dx in direct:
            ny = y + dy
            nx = x + dx
            if ny < 0 or nx < 0 or ny >= r or nx >= c:
                continue
            if board[ny][nx] in data:
                continue
            if cache[ny][nx] == data + board[ny][nx]:
                continue
            else:
                cache[ny][nx] = data + board[ny][nx]
                q.append((ny, nx, data + board[ny][nx]))
                max_size = max(max_size, len(data)+1)
    print(max_size) # len("CAD")

r, c = map(int, input().split())
cache = [['']*c for _ in range(r)]
board = []
for i in range(r):
    board.append(input())

bfs()


"""
4 4
ABCD
EFAD
ASDA
NGHZ

8
"""

