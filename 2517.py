import sys
read = sys.stdin.readline

n = int(read())
tree = [0] * (n+1)

arr = []
for i in range(n):
    x = int(read())
    arr.append([x, i])

arr.sort()
for i in range(n):
     arr[i][0] = i+1
arr.sort(key= lambda x:x[1])

for i in range(n):
    ret = 0
    pos = arr[i][0]
    while pos > 0:
        ret += tree[pos]
        pos &= (pos-1)
    print(i+1 - ret)

    pos = arr[i][0]
    while pos <= n:
        tree[pos] += 1
        pos += (pos & -pos)