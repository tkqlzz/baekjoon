n, l = map(int, input().split())

for i in range(l, 101):
    m = n//i
    s = m - (i-1)//2
    e = m + (i+2)//2
    if s >= 0 and n == (s+e-1)*i/2:
        print(' '.join(map(str, [i for i in range(s, e)])))
        exit(0)

print(-1)