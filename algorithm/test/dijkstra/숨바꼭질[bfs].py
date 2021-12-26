import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
visit = [0]*(n+1)
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)
visit[1] = 1
while q:
    now = q.popleft()
    for i in graph[now]:
        if visit[i] == 0:
            visit[i] = visit[now] + 1
            q.append(i)

m = max(visit)
print(visit.index(m),m-1,visit.count(m))
