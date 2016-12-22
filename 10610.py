s = input()

num = [0] * 10
for i in s:
    num[int(i)] += 1

if num[0]:
    x = 0
    for i in range(1, 10):
        x += num[i] * i
    if x % 3 == 0:
        s = ''
        for i in reversed(range(10)):
            s += str(i) * num[i]
        print(s)
    else:
        print(-1)
else:
    print(-1)

