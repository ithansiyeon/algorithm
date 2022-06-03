import sys
sys.stdin = open("in5.txt", "rt")
n = int(input())
data = [list(map(int,input().split(" "))) for _ in range(n)]
data.sort(reverse=True)
last = data[0][1]
cnt = n
for i in range(1,n):
    if last > data[i][1]:
        cnt-=1
    else:
        last = data[i][1]

print(cnt)