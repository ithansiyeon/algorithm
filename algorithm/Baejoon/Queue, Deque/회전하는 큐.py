from collections import deque

n,m = map(int,input().split())
poplist = deque(list(map(int,input().split())))
dlist = deque([i for i in range(1,n+1)])
cnt = 0

while len(poplist) != 0:
    if poplist[0] == dlist[0]:
        poplist.popleft()
        dlist.popleft()
    else:
        idx = dlist.index(poplist[0])
        if idx > (len(dlist) // 2):
            dlist.rotate(1)
            cnt+=1
        else:
            dlist.rotate(-1)
            cnt+=1
print(cnt)