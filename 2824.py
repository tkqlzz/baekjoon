def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

chk = 0
s = 1
for b in map(int, input().split()):
    for i in range(n):
        if arr[i] != 1:
            t = gcd(arr[i], b)
            s = s * t
            if s >= 1000000000:
                s %= 1000000000
                chk = 1
            b //= t
            arr[i] //= t
            if b == 1:
                break

result = str(s)
if chk:
    result = "0" * (9-len(result)) + result
    print(result)
else:
    print(result)
