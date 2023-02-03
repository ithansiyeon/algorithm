import sys

input = sys.stdin.readline

n = int(input())
vlist = []
h,w = 0,0
idx1, idx2 = 0,0

for i in range(6):
    a,b = map(int,input().split(" "))
    vlist.append(b)
    if a == 1 or a == 2:
        h = max(h,b)
        if h == b:
            idx1 = i
    if a == 3 or a == 4:
        w = max(w,b)
        if w == b:
            idx2 = i

shorth = abs(vlist[(idx2-1)%6] - vlist[(idx2+1)%6])
shortw = abs(vlist[(idx1-1)%6] - vlist[(idx1+1)%6])
print((h*w-shorth*shortw)*n)
