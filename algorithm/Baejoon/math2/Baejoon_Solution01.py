num = int(input())
cnt = 0
for i in list(map(int,input().split())):
    loop = True
    if i != 1:
         for j in range(2, i):
            if i % j == 0:
                loop = False
                break
    if i!= 1 and loop:
        cnt += 1
print(cnt)