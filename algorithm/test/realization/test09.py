import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
a = int(sys.stdin.readline().rstrip())
apple = [[0]*n for _ in range(n)]
for i in range(a):
    a,b = map(int,input().split(" "))
    apple[a-1][b-1] = 1
l = int(sys.stdin.readline().rstrip())
change = {}
for i in range(l):
    x,c = input().split(" ")
    change[int(x)]=c
d = 1
# 북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]
times = 0
nx,ny = 0,0
snake = deque([[0,0]])
apple[0][0] = 2
def change_direction(direction,d):
    if direction == "D":
        d = (d+1)%4
    else:
        d = (d-1)%4
    return d
while True:
    times += 1
    nx+=dx[d]
    ny+=dy[d]
    x,y= 0,0
    if 0<=nx<n and 0<=ny<n and apple[nx][ny] != 2:
        if not apple[nx][ny] == 1:
            x,y = snake.popleft()
            apple[x][y] = 0
        apple[nx][ny] = 2
        snake.append([nx,ny])
        if times in change.keys():
            d = change_direction(change[times],d)
    else:
        break
print(times)
