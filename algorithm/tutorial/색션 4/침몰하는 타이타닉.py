import sys
sys.stdin = open("in5.txt", "rt")
n,m = map(int,input().split())
boats = list(map(int,input().split()))

boats.sort()
res = 0
nlist = []

for i in range(n):
    loop = True
    for j in range(n-1,i,-1):
        if (j,boats[j]) not in nlist:
            if boats[i]+boats[j] <= m:
                nlist.append((i,boats[i]))
                nlist.append((j,boats[j]))
                res+=1
                loop = False
                break
    if loop and (i,boats[i]) not in nlist:
        nlist.append((i,boats[i]))
        res+=1

print(res)


