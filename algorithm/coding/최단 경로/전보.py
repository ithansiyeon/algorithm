import heapq

n,m,c = map(int,input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
q = []
start = c

for i in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))


def dijkstra():
    distance[start] = 0
    heapq.heappush(q,(start,0))
    while q:
        now, dist = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(i[0],cost))

dijkstra()
cnt = 0
mmax = 0

for d in distance:
    if d != INF:
        cnt+=1
        mmax = max(mmax,d)

print(cnt-1,mmax)
