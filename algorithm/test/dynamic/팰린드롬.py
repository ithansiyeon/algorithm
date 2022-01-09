import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split(" ")))
t = int(input())
dp = [[0]*n for _ in range(n)]

for i in range(n):
    for start in range(n-i):
        end = start + i
        if start == end:
            dp[start][end] = 1
        elif data[start] == data[end]:
            if start + 1 == end:
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1

for i in range(t):
    a,b = map(int,input().split(" "))
    print(dp[a-1][b-1])



