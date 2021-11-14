a,b = map(int,input().split(" "))
x,y,d = map(int,input().split(" "))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
room = []
for i in range(a):
    room.append(list(map(int,input().split(" "))))
dp = [[0]*a for _ in range(a)]
dp[x][y] = 1
x = x + dx[d]
y = y + dy[d]
def direction():
    global d
    d-=1
    if d==-1:
        d=3
cnt = 1
time_cnt = 0
while True:
    for i in range(4):
        direction()
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < a and 0<= ny < a and dp[nx][ny] == 0 and room[nx][ny] == 0:
            time_cnt = 0
            x = nx
            y = ny
            dp[nx][ny] = 1
            cnt+=1
        else:
            x = nx
            y = ny
            time_cnt+=1
    if time_cnt == 4:
        nx = x-dx[d]
        ny = y-dy[d]
        if 0<=nx-dx[d]<a and 0<=ny-dy[d]<a:
           if dp[nx][ny] == 1:
               x,y = nx,ny
           elif room[nx][ny] == 1:
               print(cnt)
               break
        else:
            print(cnt)
            break
        time_cnt = 0
    print(cnt)
sum1 = 0
