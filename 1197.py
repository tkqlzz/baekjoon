parent = dict()
rank = dict()


def make_set(v):
    parent[v] = v
    rank[v] = 0


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(v1, v2):
    root1 = find(v1)
    root2 = find(v2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def kruskal():
    for v in vertices:
        make_set(v)

    minimum_spanning_tree = set()
    edges.sort()
    for edge in edges:
        w, v1, v2 = edge
        if find(v1) != find(v2):
            union(v1, v2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree


v, e = map(int, input().split())
vertices = [i for i in range(1, v + 1)]
edges = []
for i in range(e):
    v1, v2, w = map(int, input().split())
    edges.append((w, v1, v2))

graph = {'vertices': vertices,
         'edges': edges
         }

mst = kruskal()
s = 0
for w, v1, v2 in mst:
    s += w
print(s)
print(parent)