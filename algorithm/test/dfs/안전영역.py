import sys
sys.setrecursionlimit(100000)
n = int(input())
data = []
k = 0
for i in range(n):
    data.append(list(map(int,input().split(" "))))
    k = max(k,max(data[i]))
    
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,k):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if check[x][y] == 1 and data[x][y] > k:
        check[x][y] = 0
        dfs(x - 1, y,k)
        dfs(x + 1, y,k)
        dfs(x, y - 1,k)
        dfs(x, y + 1,k)
        return True
    return False

result = 0

while k > 0:
    k-=1
    check = [[1] * n for i in range(n)]
    cnt = 0
    for i in range(n*n):
        r = i // n
        c = i % n
        if check[r][c]:
            if dfs(r,c,k):
                cnt+=1

    result = max(result,cnt)

print(result)

