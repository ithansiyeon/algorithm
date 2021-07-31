slist = []
for i in range(int(input())):
    slist.append(input())

slist = sorted(list(set(slist)))
for s in sorted(slist,key=len,reverse=False):
    print(s)
