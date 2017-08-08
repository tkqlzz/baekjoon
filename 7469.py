from math import log2, ceil
import random

def build(i, s, e):
    if s == e:
        tree[i] = [arr[s]]
    else:
        m = (s + e) // 2
        build(i*2, s, m)
        build(i*2+1, m+1, e)
        tree[i] = sorted(tree[i*2] + tree[i*2+1])


def query(l, r, i, s, e):
    if l > e or r < s:
        return []
    if l <= s and e <= r:
        return tree[i]
    m = (s + e) // 2
    return sorted(query(l, r, i*2, s, m) + query(l, r, i*2+1, m+1, e))


#n, m = map(int, input().split())
#arr = list(map(int, input().split()))
n, m = 100000, 5000
arr = [i*i for i in range(1, 100001)]
random.shuffle(arr)

tree = [None] * (1 << (ceil(log2(n)) + 1))

build(1, 0, n-1)

for x in range(1, m+1):
    i = x
    j = x*2
    k = random.randint(1, j-i)
    print(query(i - 1, j - 1, 1, 0, n - 1)[k - 1])

"""
for _ in range(m):
    i, j, k = map(int, input().split())
    print(query(i-1, j-1, 1, 0, n-1)[k-1])
"""