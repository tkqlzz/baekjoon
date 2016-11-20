def quad_tree(x, y, n):
    s = sum(([sum(arr[i][x:n+x]) for i in range(y, n+y)]))
    if s == n*n:
        print(1, end="")
    elif s == 0:
        print(0, end="")
    else:
        n_div = n // 2
        print("(",end="")
        quad_tree(x, y, n_div)
        quad_tree(x + n_div, y, n_div)
        quad_tree(x, y + n_div, n_div)
        quad_tree(x + n_div, y + n_div, n_div)
        print(")", end="")


N = int(input())
arr = [[0] * N for _ in range(N)]
for i in range(N):
    s = input()
    for j in range(N):
        arr[i][j] = int(s[j])

quad_tree(0, 0, N)