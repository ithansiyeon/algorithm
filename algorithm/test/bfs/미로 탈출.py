from collections import deque

n,m = map(int,input().split(" "))
miro = []
path = deque()
visited = [[False]*m for i in range(n)]

for i in range(n):
    miro.append(list(map(int,input())))
visited[0][0] = True
path.append([0,0])
dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = 0
while path:
    x,y = path.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                path.append([nx,ny])
                result += 1
print(miro[n-1][m-1])


