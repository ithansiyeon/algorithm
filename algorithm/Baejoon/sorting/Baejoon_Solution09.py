slist = []
for i in range(int(input())):
    slist.append(tuple(input().split()+[i]))
for i in sorted(slist,key=lambda k:(int(k[0]),int(k[-1]))):
    print(i[0],i[1])