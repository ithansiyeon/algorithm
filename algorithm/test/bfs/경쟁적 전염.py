import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split(" "))

data = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
data = []
virus = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))
    for j in range(n):
        if data[i][j] != 0:
            virus.append((data[i][j],i,j,0))

# s초 뒤에 x,y
s, x, y = map(int, input().split(" "))

virus.sort()
path = deque(virus)

while path:
    val, x1, y1, t = path.popleft()
    if t == s:
        break
    for i in range(4):
        nx = x1 + dx[i]
        ny = y1 + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if data[nx][ny] == 0:
                data[nx][ny] = val
                path.append((val,nx,ny,t+1))

print(data[x - 1][y - 1])
