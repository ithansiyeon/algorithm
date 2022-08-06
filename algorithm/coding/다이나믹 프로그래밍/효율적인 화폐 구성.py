# n,m = 2,15
# value = [2,3]

n,m = 3,4
value = [3,5,7]

dp = [1001]*1001
dp[0] = 0
for i in range(1,m+1):
    for j in value:
        dp[i] = min(dp[i-j]+1,dp[i])

if dp[m] == 1001:
    print(-1)
else:
    print(dp[m])




