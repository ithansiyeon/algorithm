import sys
from collections import Counter
from itertools import combinations

# sys.stdin = open("input.txt","rt")
n,m = map(int,input().split())
nlist = []

for i in range(1,n+1):
    for j in range(1,m+1):
        nlist.append(i+j)

slist = Counter(nlist)

cnt = 0
nlist = []

for val,idx in slist.most_common():
    if cnt < idx:
        cnt = idx
        print(val,end=' ')
    elif cnt == idx:
        print(val,end=' ')











