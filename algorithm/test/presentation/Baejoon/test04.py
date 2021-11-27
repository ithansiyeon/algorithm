num = int(input())

for i in range(num):
    def div(k, n):
        if k == 0:
            dp[k][n-1] = n
            return n
        elif n == 1:
            dp[k][n-2] = 1
            return 1
        else:
            return dp[k][n-2] + dp[k-1][n-1]

    k = int(input())
    n = int(input())
    dp = [[0]*n for i in range(k+1)]
    for i in range(k+1):
        for j in range(1,n+1):
            dp[i][j-1] = div(i,j)
    print(dp[k][n-1])

