import sys
input = sys.stdin.readline
n = int(input())
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

result = []
for i in range(n):
    cnt = 1
    for j in range(n):
        if i!=j and array[i][0] < array[j][0] and array[i][1] < array[j][1]:
            cnt+=1
    result.append(cnt)

print(" ".join(map(str,result)))