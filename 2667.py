def bfs():
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    result = []

    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                q = [[i, j]]
                arr[i][j] = 0
                cnt = 1
                while q:
                    y, x = q.pop(0)
                    for d in direct:
                        dy = y + d[0]
                        dx = x + d[1]
                        if dy < 0 or dx < 0 or dy >= n or dx >= n:
                            continue
                        if arr[dy][dx]:
                            arr[dy][dx] = 0
                            q.append([dy, dx])
                            cnt += 1
                result.append(cnt)

    result.sort()
    print(len(result))
    for i in result:
        print(i)


n = int(input())
arr = [[]]*n
for i in range(n):
    arr[i] = [int(i) for i in input()]

bfs()