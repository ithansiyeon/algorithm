import bisect

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

dp = [data[0]]

for i in range(n):
    if data[i] > dp[-1]:
        dp.append(data[i])
    else:
        idx = bisect.bisect_left(dp,data[i])
        dp[idx] = data[i]

print(n-len(dp))

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

dp = [1]*n

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(n-max(dp))

