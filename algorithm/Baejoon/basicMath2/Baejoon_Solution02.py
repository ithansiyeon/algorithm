a = int(input())
b = int(input())
slist = []
for i in range(a,b+1):
    loop = True
    if i != 1:
        for j in range(2,i):
            if i % j == 0:
                loop = False
                break
    else:
        loop = False
    if loop:
        slist.append(i)
if len(slist) != 0:
    print(sum(slist))
    print(min(slist))
else:
    print(-1)

