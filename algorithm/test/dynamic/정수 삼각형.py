n = int(input())
array = []
for i in range(n):
    array.append(list(map(int,input().split(" "))))

for i in range(1,n):
    for j in range(len(array[i])):
        if j-1 < 0:
            left = 0
        else:
            left = array[i-1][j-1]
        if j < len(array[i-1]):
            right = array[i-1][j]
        else:
            right = 0

        array[i][j] += max(left,right)


print(max(array[-1]))

