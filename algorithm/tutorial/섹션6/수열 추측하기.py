import sys

sys.stdin = open("in5.txt", "rt")
n,f = map(int,input().split())

b = [1]*n
res = [0]*n
ch = [0]*f

for i in range(1,n-1):
    b[i] = b[i-1]*(n-i)//i


def dfs(l,sum):
    if l == n and sum == f:
        for i in range(n):
            print(res[i], end=" ")
        sys.exit(0)
    else:
        for i in range(1,n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[l] = i
                dfs(l+1, sum+(res[l]*b[l]))
                ch[i] = 0

dfs(0,0)


