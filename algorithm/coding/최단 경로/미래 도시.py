import heapq

n,m = 5,7
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF]*(n+1)
q = []
start = 1

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
x,k = 4,5

def dijkstra():
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra()

if (distance[x]+distance[k]) >= INF:
    print(-1)
else:
    print(distance[x]+distance[k])





