import sys

input = sys.stdin.readline
n = int(input())
data = [0 for i in range(10001)]

for i in range(n):
    num = int(input())
    data[num] += 1

for i in range(10001):
    for j in range(data[i]):
            print(i)