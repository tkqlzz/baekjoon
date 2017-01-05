s = input()
x = input()[::-1]
x_size = len(x)
res = list(s[:x_size-1])

for i in range(x_size-1, len(s)):
    res.append(s[i])
    if res[-1] == x[0] and len(res) >= x_size:
        chk = True
        for j in range(1, x_size):
            if res[-1-j] != x[j]:
                chk = False
                break
        if chk:
            for _ in range(x_size):
                res.pop()

if res:
    print(''.join(res))
else:
    print("FRULA")