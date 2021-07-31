nlist = []
for i in range(int(input())):
    nlist.append(tuple(map(int,input().split())))

for i in sorted(nlist,key=lambda k:(k[1],k[0])):
    print(i[0],i[1])