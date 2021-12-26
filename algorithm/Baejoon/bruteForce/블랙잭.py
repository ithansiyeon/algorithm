import heapq
import sys
from itertools import combinations

input = sys.stdin.readline
n,m = map(int,input().split())
data = list(map(int,input().split()))
q = []
for i in list(combinations(data,3)):
    s = sum(i)
    if sum(i) <= m:
        heapq.heappush(q,s*(-1))
s = heapq.heappop(q)
print(s*(-1))


