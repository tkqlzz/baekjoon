for t in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())), list(map(int, input().split()))]
    dp = [[0] * n, [0] * n]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if n > 1:
        dp[0][1] = arr[0][0] + arr[1][1]
        dp[1][1] = arr[1][0] + arr[0][1]
    for i in range(2, n):
        if i % 2 == 1:
            x = 1
            y = 0
        else:
            x = 0
            y = 1
        dp[0][i] = max(arr[x][i] + dp[0][i-1], arr[x][i] + dp[1][i-2])
        dp[1][i] = max(arr[y][i] + dp[1][i-1], arr[y][i] + dp[0][i-2])
    print(max(dp[0][n-1], dp[1][n-1]))