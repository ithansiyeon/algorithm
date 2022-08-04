import sys
input = sys.stdin.readline

n = int(input())

data = []
for i in range(n):
    data.append(input())

data = list(set(data))

data = sorted(data,key = lambda x : (len(x),x))

print("".join(data))
