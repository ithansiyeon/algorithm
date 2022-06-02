import sys
from collections import deque

sys.stdin = open("in3.txt", "rt")
n,m = map(int,input().split())
boats = list(map(int,input().split()))
boats.sort()
boats = deque(boats)
cnt=0
while boats:
    if boats[0] + boats[-1] <= m and len(boats) != 1:
        cnt+=1
        boats.popleft()
        boats.pop()
    else:
        cnt+=1
        boats.pop()
print(cnt)
