n = 4
k = [1,3,1,5]

dp = [0]*100
dp[0] = k[0]
dp[1] = max(k[0],k[1])

for i in range(2,n):
    dp[i] = max(dp[i-1],k[i-2]+k[i])

print(dp[n-1])