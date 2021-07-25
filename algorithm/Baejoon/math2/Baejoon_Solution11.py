import math

for i in range(int(input())):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif math.sqrt((x2-x1)**2+(y2-y1)**2) > r1+r2:
        print(0)
    elif (x2-x1)**2+(y2-y1)**2 < (r2-r1)**2:
        print(0)
    elif (x2-x1)**2+(y2-y1)**2 == (r2-r1)**2:
        print(1)
    elif (x2-x1)**2+(y2-y1)**2 == (r2+r1)**2:
        print(1)
    elif (r1+r2) > math.sqrt((x1-x2)**2+(y1-y2)**2) > math.sqrt((r1-r2)**2):
        print(2)