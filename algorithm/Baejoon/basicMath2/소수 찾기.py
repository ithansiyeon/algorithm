n = int(input())
nlist = list(map(int,input().split(" ")))
cnt = 0
for i in nlist:
    loop = True
    if i != 1:
        for j in range(2,i):
            if i % j == 0:
                loop = False
                break
    else:
        loop = False
    if loop:
        cnt+=1
print(cnt)

