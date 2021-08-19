a = input()
b = input()
a1 = len(a)
b1 = len(b)
dp = [[0]*(b1+1) for i in range(a1+1)]
for i in range(1,a1+1):
    for j in range(1,b1+1):
        if a[i-1] != b[j-1]:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        else:
            dp[i][j]=dp[i-1][j-1]+1

print(dp[-1][-1])
