from collections import deque

n,m = 5,6
graph = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]

# 1이 괴물이 없는 부분

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(x,y):
    q = deque()
    q.append([x,y])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            else:
                if graph[nx][ny] == 1:
                    q.append([nx,ny])
                    graph[nx][ny] = graph[x][y]+1

bfs(0,0)

print(graph[n-1][m-1])
