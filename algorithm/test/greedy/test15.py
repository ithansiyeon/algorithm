from collections import Counter

n,m = map(int,input().split(" "))
slist = []
for i in range(n):
    slist.append(input())
result = ""
cnt = 0
for i in range(m):
    chr = []
    for j in range(n):
        chr.append(slist[j][i])
    chr.sort()
    result+=Counter(chr).most_common(1)[0][0]
    cnt+=sum(Counter(chr).values())-Counter(chr).most_common(1)[0][1]
print(result)
print(cnt)
