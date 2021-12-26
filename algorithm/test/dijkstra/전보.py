import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

n,m,c = map(int,input().split())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)
for i in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra():
    q = []
    heapq.heappush(q,(0,c))
    distance[c] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(i[1],i[0]))

dijkstra()
count = 0
val = 0

for i in range(n+1):
    if distance[i] != INF and distance[i] != 0:
        count+=1
        val = max(val,distance[i])

print(count,val)


