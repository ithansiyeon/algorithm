import math
n = int(input())
for i in range(n):
    a,b = map(int,input().split(" "))
    diff = b - a
    root = int(math.sqrt(diff))
    if diff <= 3:
        print(diff)
    elif diff == root**2:
        print(2*root-1)
    elif root**2+root >= diff > root**2:
        print(2*root)
    elif diff > root**2+root:
        print(2*root+1)