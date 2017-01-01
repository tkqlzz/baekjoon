import sys
read = sys.stdin.readline


def b_search(x, arr):
    low, high = 0, n // 2 - 1
    while low <= high:
        m = (low + high) // 2
        if arr[m] < x:
            low = m + 1
        else:
            high = m - 1
    return n // 2 - high - 1


n, h = map(int, read().split())
bottom = [0] * (n // 2)
top = [0] * (n // 2)
res = [987654321] + [0] * h

for i in range(n // 2):
    bottom[i] = int(read())
    top[i] = int(read())

bottom.sort()
top.sort()

for i in range(1, h + 1):
    res[i] = b_search(i, bottom) + b_search(h-i+1, top)

x = min(res)
print(x, res.count(x))
