import sys
from collections import deque
# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
n,m,k,x = map(int,sys.stdin.readline().rstrip().split(" "))
data = [[] for _ in range(n)]
visited = [False]*n
for i in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split(" "))
    data[a-1].append(b-1)

result = [0]*n
path = deque()
path.append(x-1)
answer = []
visited[x-1] = True
while path:
    now = path.popleft()
    for i in data[now]:
        if not visited[i]:
            visited[i] = True
            path.append(i)
            result[i] = result[now]+1
            if result[i] == k:
                answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i+1)

