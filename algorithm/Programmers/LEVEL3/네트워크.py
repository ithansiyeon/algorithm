def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def solution(n, computers):
    answer = 0
    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if i!=j and computers[i][j] == 1:
                union_parent(parent,i,j)
    ans = set()
    for i in range(n):
        ans.add(find_parent(parent, i))
    return len(ans)

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))