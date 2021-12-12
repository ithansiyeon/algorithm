n = int(input())
nlist = []
for i in range(n):
    nlist.append(int(input()))
nlist.sort(reverse=True)

for i in nlist:
    print(i,end=' ')