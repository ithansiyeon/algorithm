from collections import deque

def solution(maps):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque()
    r = len(maps)
    c = len(maps[0])
    q.append([0,0])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c:
                if maps[nx][ny] == 1:
                    maps[nx][ny]+=maps[x][y]
                    q.append([nx,ny])
    if maps[r-1][c-1] == 1:
        return -1
    else:
        return maps[r-1][c-1]

    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))