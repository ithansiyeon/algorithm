from collections import deque

n = int(input())

for i in range(n):
    cnt = 0
    a,b = map(int,input().split(" "))
    m = deque([0] * a)
    m[b]=1
    slist = deque(list(map(int,input().split(" "))))
    while True:
        if slist[0] == max(slist):
            cnt+=1

            if m[0] == 1:
                print(cnt)
                break
            else:
                slist.popleft()
                m.popleft()
        else:
            slist.append(slist.popleft())
            m.append(m.popleft())
