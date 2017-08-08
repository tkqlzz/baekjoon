from math import log2, ceil
import sys
read = sys.stdin.readline


def build(i, s, e):
    if s == e:
        tree[i] = arr[s]
    else:
        m = (s + e) // 2
        build(i*2, s, m)
        build(i*2+1, m+1, e)
        tree[i] = tree[i*2] + tree[i*2+1]


def query(l, r, i, s, e):
    if l > e or r < s:
        return 0
    if l <= s and e <= r:
        return tree[i]
    m = (s + e) // 2
    return query(l, r, i*2, s, m) + query(l, r, i*2+1, m+1, e)


def update(l, r, i, s, e):
    if l > e or r < s:
        return 0
    if s == e:
        tree[i] = arr[s]
        return tree[i]
    else:
        m = (s + e) // 2
        temp = update(l, r, i * 2, s, m) + update(l, r, i * 2 + 1, m + 1, e)
        tree[i] = tree[i*2] + tree[i*2+1]
        return temp


n, m = map(int, read().split())
arr = list(map(int, read().split()))

tree = [0] * (1 << (ceil(log2(n)) + 1))

build(1, 0, n-1)

for _ in range(m):
    i, *x = map(int, input().split())
    if i == 1:
        arr[x[0]-1], arr[x[1]-1] = arr[x[1]-1], arr[x[0]-1]
        res = update(x[0] - 1, x[1] - 1, 1, 0, n - 1)
    elif i == 2:
        res = query(x[0]-1, x[1]-1, 1, 0, n-1) - query(x[2]-1, x[3]-1, 1, 0, n-1)

    while res >= 2147483648:
        res -= 2147483648 * 2
    while res < -2147483648:
        res += 2147483648 * 2
    print(res)