import math
n = int(input())
result=[1,2,3]
for i in range(n):
    x,y = map(int,input().split(" "))
    diff = int(y-x)
    if diff <= 3:
        print(diff)
    else:
        n = int(math.sqrt(diff))
        if n ** 2 == diff:
            print(n*2-1)
        elif n**2 < diff <= n**2+n:
            print(2*n)
        else:
            print(2*n+1)
