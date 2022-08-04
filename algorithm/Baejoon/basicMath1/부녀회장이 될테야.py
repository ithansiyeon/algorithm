num = int(input())

for i in range(num):
    k = int(input())
    n = int(input())
    list = []
    for i in range(1,n+1):
        list.append(i)
    for i in range(k-1):
        for j in range(1,n):
            list[j]=list[j-1]+list[j]
    print(sum(list))