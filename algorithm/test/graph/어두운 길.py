n,m = map(int,input().split())

edges = []

for i in range(m):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0]*n

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,n):
    parent[i] = i

edges.sort()

result = 0
hap = 0
# 간선을 하나씩 확인하며
for edge in edges:
    cost,a,b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
    hap+=cost

print(hap-result)