def solution(m, n, puddles):
    dp = [[0]*n for i in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if [i+1,j+1] in puddles:
                dp[i][j] = 0
            else:
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1] % 1000000007

print(solution(4,3,[[2,2]])%1000000007)