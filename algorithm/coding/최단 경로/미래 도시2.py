n,m = map(int,input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
distance = [INF]*(n+1)


for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

x,k = map(int,input().split())

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

cost = graph[1][k] + graph[x][k]

if cost >= INF:
    print(-1)
else:
    print(cost)


'''
1 2
1 3
1 4
2 4
3 4
3 5
4 5
'''