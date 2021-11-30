import sys
sys.setrecursionlimit(100000)
n = int(input())
data = []
for i in range(n):
    data.append(list(input()))

# 남, 북, 동, 서
dx = [-1,1,0,0]
dy = [0,0,1,-1]

check = [[1]*n for i in range(n)]

def dfs(x,y,s):
    check[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and check[nx][ny] and s == data[nx][ny]:
            dfs(nx,ny,s)
    return None

result = 0
for i in range(n*n):
    r = i//n
    c = i%n
    if check[r][c]:
        dfs(r,c,data[r][c])
        result+=1

for i in range(n):
    for j in range(n):
        if data[i][j] == "R":
            data[i][j] = "G"
result1 = 0
check = [[1]*n for i in range(n)]
for i in range(n*n):
    r = i//n
    c = i%n
    if check[r][c]:
        dfs(r,c,data[r][c])
        result1+=1

print(result,result1)