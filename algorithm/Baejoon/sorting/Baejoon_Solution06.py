list = []
for i in range(int(input())):
    list.append((tuple(map(int,input().split()))))
for i in sorted(list,key=lambda k:(k[0],k[1])):
    print(i[0],i[1])