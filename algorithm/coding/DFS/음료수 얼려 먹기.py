graph = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]

n,m = 4,5
cnt = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    if not(0<=x<n and 0<=y<m):
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j):
            cnt+=1

print(cnt)
