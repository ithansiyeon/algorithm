from collections import deque
n = int(input())

for i in range(n):
    n,m = map(int,input().split(" "))
    queue1 = list(map(int,input().split(" ")))
    if len(queue1) == 1:
        print(1)
    else:
        alist = [[0,0] for _ in range(n)]
        for i in range(n):
            alist[i][0] = queue1[i]
            alist[i][1] = i
        deque1 = deque()
        deque1 = deque(alist)
        cnt = 0
        while deque1:
            maxx = max([i[0] for i in deque1])
            q = deque1.popleft()
            if q[0] != maxx:
                deque1.append(q)
            else:
                cnt+=1
                if q[1] == m:
                    print(cnt)
                    break




