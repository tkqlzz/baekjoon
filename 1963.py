import collections


def eratos(x):
    prime = [0, 0] + [1] * (x - 2)
    for i in range(2, int(x ** (1 / 2))):
        if prime[i]:
            for j in range(i * i, x, i):
                prime[j] = 0
    return prime


def bfs(x, y):
    visit = [0] * 10000
    visit[int(x)] = 1
    q = collections.deque()
    q.append((x, 0))
    while q:
        now, cnt = q.popleft()
        if now == y:
            return cnt
        for i in range(4):
            num = [str(i) for i in range(10)]
            num.pop(int(now[i]))
            if i == 0:
                num.pop(0)
            for j in num:
                s = now[:i] + j + now[i + 1:4]
                if s in cache and not visit[int(s)]:
                    visit[int(s)] = 1
                    q.append((s, cnt + 1))
    return 'Impossible'


cache = set()
temp = eratos(10000)
for i in range(1000, 10000):
    if temp[i]:
        cache.add(str(i))

for t_case in range(int(input())):
    a, b = input().split()
    print(bfs(a, b))