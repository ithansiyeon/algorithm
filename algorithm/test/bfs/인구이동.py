import sys
from collections import deque

n,l,r = map(int,sys.stdin.readline().rstrip().split(" "))
data = []
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().rstrip().split(" "))))

q = deque()

dx = [0,0,1,-1]
dy = [1,-1,0,0]
visited = [[False] * n for _ in range(n)]

def bfs(a,b):
    hap = []
    sum = 0
    l_hap = 0
    q.append([a, b])
    visited[a][b] = True
    while q:
        x,y = q.popleft()
        hap.append([x,y])
        sum+=data[x][y]
        l_hap+=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and l<= abs(data[nx][ny] - data[x][y]) <= r and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx,ny])

    if l_hap != 1 and sum != 0:
        for i in range(l_hap):
            data[hap[i][0]][hap[i][1]] = sum//l_hap
        return 1
    else:
        return 0
cnt = 0

while True:
    loop = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i,j):
                    loop = True
    if not loop:
        break
    else:
        cnt+=1
print(cnt)


