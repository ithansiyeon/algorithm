n = int(input())
m = int(input())
computers = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split(" "))
    computers[a-1].append(b-1)
    computers[b-1].append(a-1)

def dfs(x):
    global cnt
    for i in computers[x]:
        if i not in visited:
            visited.append(i)
            cnt+=1
            dfs(i)
visited = [0]
cnt = 0
dfs(0)
print(cnt)