m,n = map(int,input().split(" "))
list = []
for i in range(m,n+1):
    loop = True
    for j in range(2,int(i**(1/2))+1):
        if i % j == 0 and i != j:
            loop = False
            break
    if loop and i!=1:
        list.append(str(i))

print("\n".join(list))


