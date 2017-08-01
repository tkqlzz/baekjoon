import collections


def bfs():
    q = collections.deque()

    temp = set()
    for i in range(n+1):
        if terminal[i]:
            dp[i].append(0)
            temp.add(rev_tree[i][0][0])
    for i in temp:
        q.append(i)


    while q:
        i = q.popleft()
        is_next = False
        for b, v in tree[i]:
            if not dp[b]:
                is_next = True
                break
            dp[i].append(max(dp[b]) + v)
        if is_next:
            q.append(i)
            continue

        if rev_tree[i]:
            if rev_tree[i][0][0] not in q:
                q.append(rev_tree[i][0][0])
            terminal[i] = True

    res = 0
    for d in dp:
        res = max(res, sum(sorted(d, reverse=True)[:2]))
    print(res)

n = int(input())
tree = [[] for _ in range(n+1)]
rev_tree = [[] for _ in range(n+1)]
dp = [[] for _ in range(n+1)]
terminal = [False] + [True] * n

for i in range(n-1):
    a, b, v = map(int, input().split())
    tree[a].append([b, v])
    rev_tree[b].append([a, v])
    terminal[a] = False

bfs()

"""
1/7 15/4 6/10
12/0 26/19
15/28
"""
