n,m = map(int,input().split(" "))
array = []
dp = [10001]*(10001)
dp[0] = 0
for i in range(n):
    a = int(input())
    array.append(a)


for i in range(1,m+1):
    for j in array:
        dp[i]=min(1+dp[i-j],dp[i])

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])