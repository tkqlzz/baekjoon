import sys
read = sys.stdin.readline

n = int(read())
arr = read().split()
for i in range(n):
    arr[i] += ' '
rev_arr = arr[::-1]
s = ''.join(arr)
rev_s = ''.join(rev_arr)
cache = [0] * (n+1)
for i in range(1, n+1):
    cache[i] = len(arr[i-1]) + cache[i-1]
size = cache[n]
m = int(read())
for i in range(m):
    a, b = map(int, read().split())
    a = cache[a-1]
    b = cache[b]
    if s[a:b] == rev_s[size-b:size-a]:
        print(1)
    else:
        print(0)