import sys
from itertools import combinations

# sys.stdin = open("input.txt","rt")
n,k = map(int,input().split())
nlist = list(map(int,input().split()))
items = []
for i in list(combinations(nlist,3)):
    items.append(i[0]+i[1]+i[2])

items = list(set(items))

items.sort(reverse=True)

print(items[k-1])

