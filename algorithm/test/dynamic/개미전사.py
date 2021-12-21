n = int(input())

array = list(map(int,input().split(" ")))

dp = [0]*n
dp[0] = array[0]
dp[1] = max(array[0],array[1])
for i in range(n):
    dp[i]=max(dp[i-2]+array[i],+dp[n-1])

print(dp[n-1])