t = int(input())

for i in range(t):
    cnt = 0
    x1, y1, x2, y2 = map(int,input().split(" "))
    n = int(input())
    for i in range(n):
        px,py,r = map(int,input().split(" "))
        d1 = (((x1-px)**2) + ((y1-py)**2)) ** 0.5
        d2 = (((x2-px)**2) + ((y2-py)**2)) ** 0.5
        if (d1 < r and d2 > r) or (d1 > r and d2 < r):
            cnt+=1
    print(cnt)
