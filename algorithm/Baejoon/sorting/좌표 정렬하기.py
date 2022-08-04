import sys
input = sys.stdin.readline
n = int(input())

data = []
for i in range(n):
    x,y = map(int,input().split())
    data.append((x,y))

data.sort()
for i in data:
    print(i[0],i[1])

