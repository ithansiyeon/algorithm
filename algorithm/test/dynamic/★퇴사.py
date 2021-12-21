n = int(input())
time = []
pay = []
for i in range(n):
    a,b = list(map(int,input().split(" ")))
    time.append(a)
    pay.append(b)

dp = [0]*(n+1)

for i in range(n-1,-1,-1):
    if time[i]+i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(pay[i]+dp[i+time[i]],dp[i+1])

print(dp[0])

