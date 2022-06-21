n,m = map(int,input().split())
nlist = []
for i in range(n):
    nlist.append(list(map(int,input().split())))

res = []
for i in range(n):
    res.append(min(nlist[i]))

print(max(res))

# 3 3
# 3 1 2
# 4 1 4
# 2 2 2