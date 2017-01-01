import itertools

s = input()
size = len(s)
res = []
index = []
temp = []

cnt = 0
for i in range(size):
    if s[i] == '(':
        cnt += 1
        temp.append((cnt, i))
    elif s[i] == ')':
        temp.append((cnt, i))
        cnt -= 1
temp.sort()

while temp:
    _, j = temp.pop()
    _, i = temp.pop()
    index.append((i,j))

for i in index:
    setA = set(i)
    t = ''
    for j in range(size):
        if j not in setA:
            t += s[j]
    res.append(t)

for i in range(2, len(index)+1):
    for j in itertools.combinations(index, i):
        setA = set()
        for k, l in j:
            setA.add(k)
            setA.add(l)
        t = ''
        for k in range(size):
            if k not in setA:
                t += s[k]
        res.append(t)

res.sort()

for i in res:
    print(i)

"""
(0/(0))*(1+2)
1
(0/0)*(1+2)
0/(0)*(1+2)
(0/(0))*1+2
2
(0/0)*1+2
0/0*(1+2)
0/(0)*1+2
3
0/0*1+2
"""