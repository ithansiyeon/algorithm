import sys
sys.stdin = open("in5.txt", "rt")
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0
for i in range(n):
    for j in range(n):
        loop = True
        for k in range(4):
            if 0 <= i+dx[k] < n and 0 <= j + dy[k] < n:
                if a[i][j] > a[i+dx[k]][j+dy[k]]:
                    loop = True
                else:
                    loop = False
                    break
        if loop:
            cnt+=1

print(cnt)