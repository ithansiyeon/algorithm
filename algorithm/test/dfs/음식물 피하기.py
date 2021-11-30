import sys
sys.setrecursionlimit(100000)
n,m,k = map(int,input().split(" "))
data = [[0]*m for _ in range(n)]
garbage = []
for i in range(k):
    a,b = map(int,input().split(" "))
    garbage.append([a-1,b-1])
    data[a-1][b-1] = 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]
visited = [[False]*m for _ in range(n)]
result = 1
answer = 0
def dfs(x,y):
    global result
    visited[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == False and data[nx][ny] == 1:
            dfs(nx,ny)
            result+=1

for i in garbage:
    if visited[i[0]][i[1]] == False:
       dfs(i[0],i[1])
       answer = max(result,answer)
       result = 1

print(answer)