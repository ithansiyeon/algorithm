from collections import deque

def bfs(q,board):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    r = len(board)
    c = len(board[0])
    print(r,c)
    cnt = 0
    while q:
        m,m1 = q.popleft()
        x,y,x1,y1 = m[0],m[1],m1[0],m1[1]
        if (x == (r-1) and y == (c-1)) or (x1 == (r-1) and y1 == (c-1)):
            break
        for i in range(4):
            nx = x + dx[i]
            nx1 = x1 + dx[i]
            ny = y + dy[i]
            ny1 = y1 + dy[i]
            if 0<=nx<r and 0<=nx1<r and 0<=ny<c and 0<=ny1<c and board[nx][ny] == 0 and board[nx1][ny1] == 0:
                q.append([(nx,ny),(nx1,ny1)])
                cnt+=1
        if y == y1:
            for i in [-1, 1]:
                if 0<=y+i<c and board[x][y+i] == 0:
                    q.append([(x,y),(x,y+i)])
                if 0<=y1+i<c and board[x1][y1+i] == 0:
                    q.append([(x1, y1), (x1, y1 + i)])
                cnt+=1
        elif x == x1:
            for i in [-1,1]:
                if 0<=x+i<c and board[x+i][y] == 0:
                    q.append([(x,y),(x+i,y)])
                if 0<=x1+i<c and board[x1 + i][y1] == 0:
                    q.append([(x1,y1),(x1+i,y1)])
        cnt+=1
    return cnt

def solution(board):
    q = deque()
    q.append([(0,0),(0,1)])
    board[0][0] = 1
    board[0][1] = 1
    answer = bfs(q,board)
    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))