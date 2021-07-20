a = int(input())
b = int(input())
list = []
for i in range(a,b+1):
    loop = True
    for j in range(2,i):
        if i % j == 0:
            loop = False
            break
    if loop and i != 1:
        list.append(i)
if len(list):
    print(sum(list))
    print(min(list))
else:
    print(-1)
