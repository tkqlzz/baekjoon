def eratos(n):
    setA = set(i for i in range(2, n))
    for i in range(2, n):
        if i in setA:
            j = i
            while j < n:
                j += i
                if j in setA:
                    setA.remove(j)
    return setA

eraSet = eratos(1000000)
while True:
    x = int(input())
    if x == 0:
        break
    success = False
    for i in range(3, x-2):
        a = i
        b = x - i
        if a in eraSet and b in eraSet:
            success = True
            break
    if success:
        print(x, '=', a, '+', b)
    else:
        print("Goldbach's conjecture is wrong.")




