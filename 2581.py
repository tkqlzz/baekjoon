def eratos(n):
    setA = set(i for i in range(2, n+1))
    for i in range(2, n+1):
        if i in setA:
            j = i
            while j <= n:
                j += i
                if j in setA:
                    setA.remove(j)
    return setA

m = int(input())
n = int(input())

result = []
for i in eratos(n):
    if m <= i <= n:
        result.append(i)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)
