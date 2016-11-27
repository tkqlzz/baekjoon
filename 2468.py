import collections


def bfs():
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    max_cnt = 1
    for t in reversed(range(minN, maxN)):
        cnt = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] > t:
                    matrix[i][j] = t

                    q = collections.deque()
                    q.append((i, j))
                    cnt += 1

                    while q:
                        y, x = q.popleft()
                        for dy, dx in direct:
                            ny = y + dy
                            nx = x + dx
                            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                                continue
                            if matrix[ny][nx] > t:
                                matrix[ny][nx] = t
                                q.append((ny, nx))
        max_cnt = max(cnt, max_cnt)

    print(max_cnt)

n = int(input())
maxN = 0
minN = 100
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
    minN = min(min(matrix[i]), minN)
    maxN = max(max(matrix[i]), maxN)

bfs()

"""
3 3
ABC
BCC
CDE
"""

