n = int(input())
array = list(map(int,input().split(" ")))

array.reverse()

dp = [1]*n
# dp[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))
