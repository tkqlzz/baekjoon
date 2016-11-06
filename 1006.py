T = int(input())
for i in range(0, T):
    arr = input().split()
    N = int(arr[0])
    W = int(arr[1])
    x = 0
    list = [0]
    list += [int(n) for n in input().split()]
    list += [int(n) for n in input().split()]
    cache = list
    for i in range(1, N*2+1):
        if list[i] == 0:
            pass
        else:
            a = i - 1
            b = i + 1
            c = i - N
            if i % N == 1:
                a = i + N-1
            if i % N == 0:
                b = i - N+1
            if i <= N:
                c = i - (N+1)
            if W >= list[i] + list[a] and list[a] != 0:
                list[i] = 0
                list[a] = 0
                x += 1
            elif W >= list[i] + list[b] and list[b] != 0:
                list[i] = 0
                list[b] = 0
                x += 1
            elif W >= list[i] + list[c] and list[c] != 0:
                list[i] = 0
                list[c] = 0
                x += 1
    for i in range(1, N*2+1):
        if list[i] == 0:
            pass
        else:
            list[i] = 0
            x += 1
    print(x)
