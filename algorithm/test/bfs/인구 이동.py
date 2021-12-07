import sys
from collections import deque

n,l,r = map(int,sys.stdin.readline().rstrip().split(" "))
data = [[] for _ in range(n)]
for i in range(n):
    data[i] = list(map(int,sys.stdin.readline().rstrip().split(" ")))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(a,b):
    q = deque()
    global hap
    loop = False
    q.append([a,b])
    q1 = []
    cnt = 0
    while q:
        x,y = q.popleft()
        q1.append([x, y])
        hap += data[x][y]
        visited[x][y] = True
        cnt+=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and l <= abs(data[x][y] - data[nx][ny]) <= r:
                loop = True
                q.append([nx,ny])
    avg = hap // cnt
    while q1:
        x,y = q1.pop()
        data[x][y] = avg
    if not loop:
        return False
    else:
        return True
ans = 0

while True:
    visited = [[False] * n for _ in range(n)]
    loop = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                hap = 0
                result = bfs(i,j)
                if result:
                    loop = True
    if not loop:
        break
    else:
        ans+=1
# print(data)
print(ans)




