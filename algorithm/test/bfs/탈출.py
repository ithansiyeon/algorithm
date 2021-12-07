from collections import deque

r,c = map(int,input().split(" "))
data = []
q = deque()
water = deque()
visited = [[False]*c for _ in range(r)]

# 물이 찬 지역 : *, 돌 : X, 비버의 굴: D, 고슴도치의 위치: S
for i in range(r):
    data.append(list(input()))
    for j in range(c):
        if data[i][j] == 'S':
            q.append([i,j,0])
            visited[i][j] = True
            data[i][j] = '.'
        elif data[i][j] == '*':
            water.append([i,j])

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def change():
    global water
    global data
    water1 = deque()
    while water:
        x,y = water.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c:
                if data[nx][ny] == '.':
                    data[nx][ny] = '*'
                    water1.append([nx,ny])
    water = water1

def bfs(q):
    global data
    while q:
        qlen = len(q)
        while qlen:
            x,y,t = q.popleft()
            if data[x][y] == 'D':
                return t
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:
                    if data[nx][ny] != '*' and data[nx][ny] != 'X':
                        visited[nx][ny] = True
                        q.append([nx,ny,t+1])
            qlen-=1
        change()
    return None
change()
answer = bfs(q)
if answer != None:
    print(answer)
else:
    print('KAKTUS')