n,m = map(int,input().split(" "))
nlist = [True for _ in range(1,m+2)]
for i in range(2,m+1):
    if nlist[i]:
        for j in range(i*2,m+1,i):
            nlist[j] = False

for i in range(n,len(nlist)):
    if nlist[i] and i > 1:
        print(i)