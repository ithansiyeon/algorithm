import sys
from itertools import combinations

# sys.stdin = open("input.txt","rt")
n = int(input())
nlist = list(map(int,input().split()))

avg = round(sum(nlist)/n)
val = 100
stu = -1
for i in range(n):
    if val > abs(nlist[i]-avg):
        stu = i
        val = abs(nlist[i]-avg)
    elif val == abs(nlist[i]-avg):
        if nlist[i] > nlist[stu]:
            stu = i
            val = abs(nlist[i] - avg)

print(avg,stu+1)
