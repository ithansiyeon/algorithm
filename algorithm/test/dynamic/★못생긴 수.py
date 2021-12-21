n = int(input())

dp = [0]*(n+1)
dp[1] = 1
i2 = i3 = i5 = 1
one,two,three = 2,3,5

for i in range(2,n+1):
    dp[i] = min(one,two,three)
    if dp[i] == one:
        i2+=1
        one = dp[i2]*2
    if dp[i] == two:
        i3+=1
        two = dp[i3]*3
    if dp[i] == three:
        i5+=1
        three = dp[i]*5

print(dp[n])



print(dp[n])