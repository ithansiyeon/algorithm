import sys

n,m = map(int,input().split(" "))
arr = [[] for _ in range(n)]
visited = [False]*n
for i in range(m):
    a,b = map(int,input().split(" "))
    arr[a].append(b)
    arr[b].append(a)

def dfs(x,depth):
    if depth == 4:
        print(1)
        sys.exit(0)
    for i in arr[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i,depth+1)
            visited[i] = False # 재귀의 끝까지 확인했는데 depth가 4가 되지 않는 상태

for i in range(n):
    visited[i] = True
    dfs(i,0)
    visited[i]=False


print(0)




