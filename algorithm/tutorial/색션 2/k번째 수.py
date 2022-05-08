import sys

#sys.stdin = open("input.txt","rt")
t = int(input())
for i in range(t):
    n,s,e,k = map(int,input().split())
    nlist = list(map(int,input().split()))
    slist = nlist[s-1:e]
    slist.sort()
    print("#{} {}".format(i+1,slist[k-1]))


