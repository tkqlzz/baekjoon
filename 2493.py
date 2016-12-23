def check(x):
    for i in reversed(stack):
        if arr[x] <= arr[i]:
            return ' ' + str(i+1)
        else:
            stack.pop()
    return ' 0'


n = int(input())
arr = []
while len(arr) != n:
    arr += list(map(int, input().split()))
stack = [0]
res = '0'
for i in range(1, n):
    res += check(i)
    stack.append(i)
print(res)