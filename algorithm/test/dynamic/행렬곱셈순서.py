import math
import sys

input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))

dp = [[0]*n for _ in range(n)]

for diagonal in range(1,n):
    for i in range(n-diagonal):
        j = i + diagonal
        dp[i][j] = math.inf
        for k in range(i,j):
            dp[i][j] = min(dp[i][j],dp[i][k]+dp[k+1][j]+data[i][0]*data[k][1]*data[j][1])
print(dp[0][n-1])


