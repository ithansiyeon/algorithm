import sys
sys.stdin = open("in5.txt", "rt")
nlist = [i for i in range(0,21)]
for i in range(10):
    a,b = map(int,input().split())
    nlist = nlist[:a]+nlist[b:a-1:-1]+nlist[b+1:]

for i in nlist[1:]:
    print(i,end=' ')