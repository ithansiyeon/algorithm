n,m = 4,4
x,y,d = 1,1,0
data = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]

map = [[0]*m for _ in range(n)]
# 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]
map[x][y] = 1
cnt = 1
turn_cnt = 0
def turn_left():
    global d
    d-=1
    if d == -1:
        d = 3

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    if map[nx][ny] == 0 and data[nx][ny] == 0:
        x = nx
        y = ny
        map[x][y] = 1
        cnt+=1
        turn_cnt = 0
        continue
    else:
        turn_cnt+=1

    if turn_cnt == 4:
        nx = x-dx[d]
        ny = y-dy[d]
        if data[nx][ny] == 0:
            x=nx
            y=ny
        else:
            break
        turn_cnt = 0

print(cnt)



