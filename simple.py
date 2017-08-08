import sys
read = sys.stdin.readline


n, m = map(int, read().split())
arr = [0] + list(map(int, read().split()))

for _ in range(m):
    i, *x = map(int, read().split())
    if i == 1:
        a, b = x
        res = sum(arr[a:b+1])

        arr[a], arr[b] = arr[b], arr[a]
    elif i == 2:
        a, b, c, d = x
        res = sum(arr[a:b+1]) - sum(arr[c:d+1])

    while res >= 2147483648:
        res -= 2147483648 * 2
    while res < -2147483648:
        res += 2147483648 * 2
    print(res)

