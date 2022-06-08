import sys

sys.stdin = open("in5.txt", "rt")
n,k = map(int,input().split())
nlist = [i for i in range(1,n+1)]
cnt = 0
while len(nlist)!= 1:
    cnt+=1
    if cnt == k:
        nlist.pop(0)
        cnt = 0
    else:
        nlist.append(nlist.pop(0))


print(nlist[0])

