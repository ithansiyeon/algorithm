import collections
import sys
sys.stdin = open("input","rt")

n = int(input())
nums = []
result = []
for i in range(n):
    nums = input().split()
    snums = list(set(nums))
    if len(snums) == 3:
        result.append(10000+int(snums[0])*1000)
    elif len(snums) == 2:
        cnums = collections.Counter(snums)
        result.append(1000+int(cnums.most_common(1)[0][0])*100)
    else:
        result.append(int(max(snums))*100)

print(max(result))
