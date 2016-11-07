n = int(input())
matrix = [list(map(int, input().split())) for row in range(n)]
cache = [[0]*row for row in range(1, n+2)]

for r in range(n-1,-1,-1):
    for c in range(r+1):
        cache[r][c] = matrix[r][c] + max(cache[r+1][c],cache[r+1][c+1])

print(cache[0][0])