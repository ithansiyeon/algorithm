import sys
input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    data.append(input().split(" ")+[i+1])

data = sorted(data,key = lambda x : (int(x[0]),x[2]))

for i in data:
    print(i[0],i[1],end="")