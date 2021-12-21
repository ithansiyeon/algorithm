n,k = map(int,input().split(" "))
array = []
dp = [0]*(k+1)
dp[0] = 1
for i in range(n):
    array.append(int(input()))

for j in range(n):
    for i in range(1,k+1):
        if i-array[j] >= 0:
            dp[i]+=dp[i-array[j]]

print(dp[k])