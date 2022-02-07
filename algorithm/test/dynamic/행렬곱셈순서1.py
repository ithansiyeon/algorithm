import math
import sys
input = sys.stdin.readline
n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))

dp = [[0]*n for _ in range(n)]

for diagonal in range(1,n):
    for i in range(n-diagonal):
        j = i+diagonal
        print(i,j)
        dp[i][j] = math.inf
        for k in range(i,j):
            dp[i][j] = min(dp[i][j],dp[i][k] + dp[k+1][j] + matrix[i][0]*matrix[k][1]*matrix[j][1])
# for i in dp:
#     print(*i)
print(dp[0][-1])

