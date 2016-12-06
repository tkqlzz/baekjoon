import sys
read = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    root1 = find(a)
    root2 = find(b)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

n, m = map(int, read().split())
parent = [i for i in range(n+1)]  # 부모
rank = [0 for i in range(n+1)]    # 트리의 깊이

for i in range(m):
    o, a, b = map(int, read().split())
    if o:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

    else:
        union(a, b)
