from math import log2, ceil
import sys
read = sys.stdin.readline


def min_build(node, start, end):
    if start == end:
        min_tree[node] = arr[start]
        return min_tree[node]
    else:
        min_tree[node] = min(min_build(node * 2, start, (start + end) // 2),
                             min_build(node * 2 + 1, (start + end) // 2 + 1, end))
        return min_tree[node]


def max_build(node, start, end):
    if start == end:
        max_tree[node] = arr[start]
        return min_tree[node]
    else:
        max_tree[node] = max(max_build(node * 2, start, (start + end) // 2),
                             max_build(node * 2 + 1, (start + end) // 2 + 1, end))
        return max_tree[node]


def query_min(left, right, node, start, end):
    if left > end or right < start:
        return 9876543210
    if left <= start and end <= right:
        return min_tree[node]
    return min(query_min(left, right, node * 2, start, (start + end) // 2),
               query_min(left, right, node * 2 + 1, (start + end) // 2 + 1, end))


def query_max(left, right, node, start, end):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return max_tree[node]
    return max(query_max(left, right, node * 2, start, (start + end) // 2),
               query_max(left, right, node * 2 + 1, (start + end) // 2 + 1, end))


n, m = map(int, read().split())
arr = [0] * n
min_tree = [0] * (1 << (ceil(log2(n)) + 1))
max_tree = [0] * (1 << (ceil(log2(n)) + 1))

for i in range(n):
    arr[i] = int(read())

min_build(1, 0, n - 1)
max_build(1, 0, n - 1)
print(min_tree)

for i in range(m):
    a, b = map(int, read().split())
    print(query_min(a-1, b-1, 1, 0, n-1), query_max(a-1, b-1, 1, 0, n-1))

