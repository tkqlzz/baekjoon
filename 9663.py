def is_promising(row):
    for i in range(row):
        if arr[i] == arr[row]:
            return False
        if arr[i] - arr[row] == row - i:
            return False
        if arr[row] - arr[i] == row - i:
            return False
    return True


def dfs(row):
    if row == n:
        global cnt
        cnt += 1
    else:
        for i in range(n):
            arr[row] = i
            if is_promising(row):
                dfs(row + 1)

cnt = 0
n = int(input())
arr = [0] * n
dfs(0)
print(cnt)

