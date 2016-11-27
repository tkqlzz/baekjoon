n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

check = arr.pop()
cnt = 1
while m > 0:
    for i in reversed(range(len(arr))):
        if check != arr[i]:
            break
        else:
            arr.pop()
            cnt += 1
    check -= 1
    m -= cnt
print(check)