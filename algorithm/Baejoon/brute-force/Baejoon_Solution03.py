num = int(input())
list = []
for i in range(num):
    list.append(tuple(map(int,input().split())))
rank = [0 for i in range(num)]
for i in range(num):
    cnt = 0
    for j in range(num):
        if i != j:
            if list[i][0] < list[j][0] and list[i][1] < list[j][1]:
                cnt+=1
    rank[i] = str(cnt+1)
print(" ".join(rank))