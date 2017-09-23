n, l = map(int, input().split())

res = [-1]
for i in range(l, 101):
    mid = n//i
    s = mid - (i-1)//2
    e = mid + (i+2)//2
    if s >= 0 and n == sum(i for i in range(s, e)):
        res = [i for i in range(s, e)]
        break

print(' '.join(map(str, res)))