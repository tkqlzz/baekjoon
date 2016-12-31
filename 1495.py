n, s, m = map(int, input().split())
arr = list(map(int, input().split()))
cache = {s}
for i in arr:
    temp = set()
    while cache:
        x = cache.pop()
        if x + i <= m:
            temp.add(x+i)
        if 0 <= x - i:
            temp.add(x-i)
    cache = temp
    if not cache:
        print(-1)
        exit(0)
print(max(cache))