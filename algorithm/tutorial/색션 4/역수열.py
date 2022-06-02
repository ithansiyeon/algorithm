import sys
sys.stdin = open("in1.txt", "rt")
n = int(input())
a = list(map(int,input().split()))
res = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if res[j] == 0 and a[i] == 0:
            res[j] = i+1
            break
        elif res[j]==0:
            a[i]-=1

print(res)