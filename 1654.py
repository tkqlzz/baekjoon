import sys


def divide():
    first, mid, last = 0, 0, sum(arr)*2 // n
    while first <= last:
        mid = (first+last) // 2
        cnt = 0
        for i in arr:
            cnt += i // mid
        if cnt < n:
            last = mid - 1
        else:
            result = mid
            first = mid + 1

    print(result)




k, n = map(int, input().split())
arr = [0] * k
for i in range(k):
    arr[i] = int(sys.stdin.readline())

arr.sort(reverse=True)

divide()