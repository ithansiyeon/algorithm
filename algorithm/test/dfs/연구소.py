import copy

n,m = map(int,input().split(" "))
lab = []
result = 0
temp = [[0]*m for i in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
virus_list = []

for i in range(n):
    lab.append(list(map(int,input().split(" "))))
for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            virus_list.append([i,j])

def virus(x,y,temp):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if temp[nx][ny] == 0:
               temp[nx][ny] = 2
               virus(nx,ny,temp)

def dfs(start,count):
    global result
    if count == 3:
        temp = copy.deepcopy(lab)
        for i in range(len(virus_list)):
            r,c = virus_list[i]
            virus(r,c,temp)
        result = max(result,sum(_.count(0) for _ in temp))
        return
    else:
        for i in range(start,n*m):
            r = i // m
            c = i % m
            if lab[r][c] == 0:
                lab[r][c] = 1
                count+=1
                dfs(i,count)
                lab[r][c] = 0
                count-=1

dfs(0,0)
print(result)