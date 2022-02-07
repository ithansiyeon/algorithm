import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
data.sort()
print(round(sum(data)/n))
print(data[n//2])
result = Counter(data).most_common(2)
if len(result) == 1 or result[0][1] != result[1][1]:
    print(result[0][0])
else:
    print(result[1][0])
print(data[-1]-data[0])