import queue
import sys
read = sys.stdin.readline

n, m = map(int, read().split())

graph = [[] for i in range(n+1)]
rev_graph_cnt = [0] * (n+1)

for i in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    rev_graph_cnt[b] += 1

pq = queue.PriorityQueue()
for i in range(1, n+1):
    if not rev_graph_cnt[i]:
        pq.put(i)

res = ''
while not pq.empty():
    i = pq.get()
    res += str(i) + ' '
    for j in graph[i]:
        rev_graph_cnt[j] -= 1
        if not rev_graph_cnt[j]:
            pq.put(j)

print(res)