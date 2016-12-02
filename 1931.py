import sys
read = sys.stdin.readline

n = int(read())
arr = []
for i in range(n):
    a, b = map(int, read().split())
    arr.append((b, a))

arr.sort()

y_min, cnt = 0, 0
for b, a in arr:
    if a >= y_min:
        y_min = b
        cnt += 1

print(cnt)
