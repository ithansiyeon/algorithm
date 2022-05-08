import sys
sys.stdin = open("in5.txt", "rt")
n = int(input())
nlist = list(map(int,input().split()))
grade = 0
loop = True
sum = 0
for i in range(n):
    if nlist[i] == 1:
        if loop == True:
            grade += 1
        else:
            grade += 1
            loop = True
    else:
        if loop == True:
            grade = 0
            loop = False
        else:
            loop = False
            grade = 0
    sum+=grade

print(sum)
