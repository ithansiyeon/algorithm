import math
dp = [1]*(246912+1)
n = int(math.sqrt(246912))
for i in range(2,n+1):
    if dp[i]:
        for j in range(2*i,246912+1,i):
            dp[j] = 0
while True:
    num = int(input())
    cnt = 0
    if num == 0:
        break
    print(sum(dp[num+1:2*num+1]))
