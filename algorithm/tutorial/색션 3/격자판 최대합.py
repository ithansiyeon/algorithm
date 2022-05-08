import sys
sys.stdin = open("in1.txt", "rt")
n = int(input())
nlist = []
for i in range(n):
    nlist.append(list(map(int,input().split())))

dx = [0,0,1,-1,1,-1]
dy = [1,-1,0,0,1,-1]

result = 0
for i in range(n):
    sum = 0
    for j in range(6):
        nx = i
        ny = 0
        sum = 0
        while True:
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                break
            sum += nlist[nx][ny]
            nx += dx[j]
            ny += dy[j]
        result = max(result,sum)
    sum = 0
    for j in range(6):
        nx = 0
        ny = i
        sum = 0
        while True:
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                break
            sum += nlist[nx][ny]
            nx += dx[j]
            ny += dy[j]
        result = max(result, sum)

print(result)


