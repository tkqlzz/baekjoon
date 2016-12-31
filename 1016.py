x, y = map(int, input().split())

n = int(y ** 0.5)
prime = set(i for i in range(2, n+1))
square_nono = set(i for i in range(x, y+1))

for i in range(2, n+1):
    if i in prime:
        j = i
        while j <= n:
            j += i
            if j in prime:
                prime.remove(j)

for i in prime:
    i = i*i
    j = i
    if j <= x:
        j *= round(x / j + 0.49)
    while j <= y:
        if j in square_nono:
            square_nono.remove(j)
        j += i

print(len(square_nono))
