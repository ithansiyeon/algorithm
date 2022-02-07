import heapq
INF = int(1e9)
cnt = 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dijkstra():
    q = []
    heapq.heappush(q,(graph[0][0],0,0))
    distance[0][0] = graph[0][0]
    while q:
        dist,x,y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q,(cost,nx,ny))

while True:
    n = int(input())
    if n == 0:
        break
    graph = []
    for i in range(n):
        graph.append(list(map(int,input().split())))
    distance = [[INF]*n for _ in range(n)]
    dijkstra()
    if distance[-1][-1] != INF:
        print("Problem {0}: {1}".format(cnt,distance[-1][-1]))
    cnt+=1
