from collections import deque

#n, m = 5000, 3
n, m = map(int, input().split())
#arr = [i for i in range(1, n+1)]

dq = deque([i for i in range(1, n+1)])

res = '<'
i = 0
while dq:
    i += 1
    if i % m == 0:
        res += str(dq.popleft()) + ", "
    else:
        dq.append(dq.popleft())

res = res[:-2] + '>'
#res += '>'
#res = res.replace(', >', '>')

print(res)