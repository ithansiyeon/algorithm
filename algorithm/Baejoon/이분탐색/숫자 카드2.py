import sys
input = sys.stdin.readline
n = int(input())
nlist = list(map(int,input().split(" ")))
m = int(input())
mlist = list(map(int,input().split(" ")))

dict = {}

for i in range(n):
    if nlist[i] in dict.keys():
        dict[nlist[i]] += 1
    else:
        dict[nlist[i]] = 1

for i in mlist:
    if i not in dict.keys():
        print(0,end=" ")
    else:
        print(dict[i],end=" ")
