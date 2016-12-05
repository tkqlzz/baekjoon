from math import log2, ceil
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)


def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        tree[node] = build(node * 2, start, int((start + end) / 2)) \
                     + build(node * 2 + 1, int((start + end) / 2) + 1, end)
        return tree[node]


def query_sum(left, right, node, start, end):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return query_sum(left, right, node * 2, start, int((start + end) / 2)) \
           + query_sum(left, right, node * 2 + 1, int((start + end) / 2) + 1, end)


def update(index, diff, node, start, end):
    if index < start or index > end:
        return
    tree[node] = tree[node] + diff
    if start != end:
        update(index, diff, node * 2, start, int((start + end) / 2))
        update(index, diff, node * 2 + 1, int((start + end) // 2) + 1, end)


n, m, k = map(int, read().split())
arr = [0] * n
tree = [0] * (1 << (ceil(log2(n)) + 1))

for i in range(n):
    arr[i] = int(read())
build(1, 0, n - 1)

for i in range(m + k):
    a, b, c = map(int, read().split())
    if a == 1:
        diff = c - arr[b-1]
        arr[b-1] = c
        update(b-1, diff, 1, 0, n-1)
    elif a == 2:
        print(query_sum(b-1, c-1, 1, 0, n-1))
