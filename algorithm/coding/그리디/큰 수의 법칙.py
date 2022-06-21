n,m,k = map(int,input().split())
nlist = list(map(int,input().split()))
nlist.sort(reverse=True)

count = int(m//(k+1))*k
count += m%(k+1)

res = 0
res += count*nlist[0]
res += (m-count)*nlist[1]

print(res)