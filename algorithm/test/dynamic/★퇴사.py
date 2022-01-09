n = int(input())
time = []
pay = []
for i in range(n):
    a,b = map(int,input().split(" "))
    time.append(a)
    pay.append(b)

dp = [0]*(n+1)

for i in range(n-1,-1,-1):
    t = i+1+time[i]
    if t <= (n+1):
        dp[i] = max(dp[i+1],pay[i]+dp[time[i]+i])
    else:
        dp[i] = dp[i+1]

print(dp[0])