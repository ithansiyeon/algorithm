import sys
#sys.stdin = open("input.txt","rt")
n = int(input())
nlist = [True]*(n+2)
for i in range(2,n+1):
    if nlist[i]:
        for j in range(i+i,n+1,i):
            nlist[j]=False
print(sum(1 for i in range(2,n+1) if nlist[i] == True))







