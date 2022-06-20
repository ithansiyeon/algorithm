n,m,k = map(int,input().split())
nlist = list(map(int,input().split()))
nlist.sort(reverse=True)
cnt = 0
res = 0

while cnt != m:
    for i in range(k):
        if cnt == m:
            break
        res+=nlist[0]
        cnt+=1
    if cnt == m:
        break
    res+=nlist[1]
    cnt+=1

print(res)