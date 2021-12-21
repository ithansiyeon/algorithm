n,m = map(int,input().split(" "))
array = []
for i in range(n):
    array.append(list(map(int,input())))

for i in range(1,n):
    for j in range(1,m):
        if array[i][j] == 1:
            array[i][j] = min(array[i-1][j-1],array[i-1][j],array[i][j-1])+1

answer = 0

for i in range(n):
    temp = max(array[i])
    answer = max(answer,temp)

print(answer**2)


