from collections import deque

n = int(input())

dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

for i in range(n):
    l = int(input())
    x,y = map(int,input().split(" "))
    tx,ty = map(int,input().split(" "))
    q = deque()
    q.append([x,y,0])
    visited = [[False]*l for _ in range(l)]
    visited[x][y] = True
    while q:
        x1,y1,t = q.popleft()
        if x1 == tx and y1 == ty:
            print(t)
            break
        for k in range(8):
            nx = x1 + dx[k]
            ny = y1 + dy[k]
            if 0 <= nx < l and 0<= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx,ny,t+1])



