import sys
from collections import deque

r,c = map(int,sys.stdin.readline().rstrip().split(" "))
water = deque()
q = deque()
data = deque()
visited = [[False]*c for _ in range(r)]
dx= [-1,1,0,0]
dy = [0,0,1,-1]
for i in range(r):
    data.append(list(sys.stdin.readline().rstrip()))
    for j in range(c):
        if data[i][j] == '*':
            water.append([i,j])
        if data[i][j] == 'S':
            q.append([i,j,0])

def bfs(q):
    global water
    while q:
        water1 = deque()
        while water:
            x,y = water.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                if data[nx][ny] == 'S' or data[nx][ny] == '.':
                    data[nx][ny] = '*'
                    water1.append([nx,ny])
        water = water1
        q_next = deque()
        for i in range(r):
            for j in range(c):
                print(data[i][j],end='')
            print()
        print()
        while q:
            x,y,cnt = q.popleft()
            visited[x][y] = True
            data[x][y] = '.'
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                if (data[nx][ny] == '.' or data[nx][ny] == 'D') and not visited[nx][ny]:
                    if data[nx][ny] == 'D':
                        return cnt+1
                    data[nx][ny] = 'S'
                    q_next.append([nx,ny,cnt+1])
        for i in range(r):
            for j in range(c):
                print(data[i][j],end='')
            print()
        print()
        q = q_next

    return None
value = bfs(q)
if value == None:
    print("KAKTUS")
else:
    print(value)



