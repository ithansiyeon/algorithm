import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

distance = [INF]*(n+1)

q = []
heapq.heappush(q,(0,1))
distance[1] = 0

while q:
    dist, now = heapq.heappop(q)
    if dist < distance[now]:
        continue

    for i in graph[now]:
        cost = dist + i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

val = max(distance[1:])
nlist = []
for i in range(1,n+1):
    if val == distance[i]:
        nlist.append(i)

print(min(nlist),val,len(nlist))


# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2