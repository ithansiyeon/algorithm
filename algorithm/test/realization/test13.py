from collections import deque
n = int(input())
a = int(input())
apple = [[0]*n for _ in range(n)]

for i in range(a):
    c,d = map(int,input().split(" "))
    apple[c-1][d-1] = 1
b = int(input())
direct= {}
for i in range(b):
    c,d = input().split(" ")
    direct[int(c)] = d

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d = 1
snake = deque([(0,0)])

nx,ny = 0,0

def change(status):
    global d
    if status == 'L':
        d=(d-1)%4
    else:
        d=(d+1)%4

time = 0
while True:
    time+=1
    nx += dx[d]
    ny += dy[d]
    print(nx,ny)
    if time in direct.keys():
        change(direct[time])
    if 0<=nx<n and 0<=ny<n and (nx,ny) not in snake:
        snake.append((nx, ny))
        if apple[nx][ny] == 1:
            apple[nx][ny] = 0
        else:
            snake.popleft()
    else:
        print(time)
        break



