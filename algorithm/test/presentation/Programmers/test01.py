def dfs(visited,x,computers):
    visited[x] = 1
    for y in range(len(computers)):
        if x != y and computers[x][y] == 1 and visited[y] == 0:
            dfs(visited,y,computers)

def solution(n, computers):
    cnt = 0
    visited = [0]*n
    for x in range(n):
        if visited[x] == 0:
                cnt+=1
                dfs(visited,x,computers)
    return cnt

solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])