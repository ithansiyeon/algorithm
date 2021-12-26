import heapq
import sys
input = sys.stdin.readline
t = int(input())
INF = int(1e9)
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(t):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    distance = [[INF]*n for _ in range(n)]

    q = []
    heapq.heappush(q,(graph[0][0],0,0))
    distance[0][0] = graph[0][0]
    while q:
        dist,x,y = heapq.heappop(q)
        if x == n-1 and y == n-1:
            print(distance[x][y])
            break
        if dist > distance[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q,(cost,nx,ny))

