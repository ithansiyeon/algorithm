from collections import Counter
import sys
import statistics
n = int(sys.stdin.readline())
list1 = []
dic = {}
for i in range(n):
    list1.append(int(sys.stdin.readline()))
    if str(list1[i]) in dic.keys():
        dic[str(list1[i])]+=1
    else:
        dic[str(list1[i])]=1

list1.sort()
c = Counter(list1)
list2 = [k for k, v in c.items() if max(c.values()) == v]
list3 = sorted(list(set(list2)))
print(round(statistics.mean(list1)))
print(statistics.median(list1))
print(list3[1] if len(list3) != 1 else list3[0])
print(list1[-1]-list1[0])