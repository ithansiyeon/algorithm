import sys

sys.stdin = open("in5.txt", "rt")
n,m = map(int,input().split())
data = list(map(int,input().split()))
data = [(data[i],i) for i in range(n)]
cnt = 0
while data:
    p = data.pop(0)
    loop = True
    for d in data:
        if p[0] < d[0]:
            data.append(p)
            loop = False
            break
    if loop:
        cnt+=1
        if p[1] == m:
            print(cnt)
