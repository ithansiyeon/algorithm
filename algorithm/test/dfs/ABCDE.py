import sys

n,m = map(int,input().split(" "))
friend = [[] for _ in range(n)]
visited = [False for _ in range(n)]
stack = []
for i in range(m):
    a,b = map(int,input().split(" "))
    friend[a].append(b)
    friend[b].append(a)

def dfs(x,depth):
    if depth == 4:
        print(1)
        sys.exit(0)
    for i in friend[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i,depth+1)
            visited[i] = False

for i in range(n):
    if not visited[i]:
        visited[i] = True
        dfs(i,0)
        visited[i] = False

print(0)


