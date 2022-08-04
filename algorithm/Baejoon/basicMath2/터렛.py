import math

n = int(input())
for i in range(n):
    x1,y1,r1,x2,y2,r2 = map(int,input().split(" "))
    r = math.sqrt((x1-x2)**2+(y1-y2)**2)
    if (0 <= r < abs(r1-r2) and r1!=r2) or r > r1+r2:
        print(0)
    elif (r == abs(r1-r2) and r!=0) or r == r1+r2:
        print(1)
    elif abs(r1-r2) < r < r1+r2:
        print(2)
    elif r1==r2:
        print(-1)