n,m = map(int,input().split())

byte = list(map(int,input().split()))
cost = list(map(int,input().split()))

dp = [[0]*(sum(cost)+1) for _ in range(n+1)]
c = sum(cost)
result = c
for i in range(1,n+1):
    for j in range(1,c+1):
        if j < cost[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(byte[i-1]+dp[i-1][j-cost[i-1]],dp[i-1][j])
        if dp[i][j] >= m:
            result = min(result,j)

if m!=0:
    print(result)
else:
    print(0)




