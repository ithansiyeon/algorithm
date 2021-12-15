import sys

n,m = map(int,sys.stdin.readline().rstrip().split(" "))
array = list(map(int,sys.stdin.readline().rstrip().split(" ")))

start = max(array)
end = sum(array)
result = 0

while start <= end:
    sum = 0
    cnt = 1
    mid = (start+end)//2
    for i in range(n):
        if sum + array[i] > mid:
            sum = 0
            cnt+=1
        sum+=array[i]

    if cnt > m:
        start = mid + 1
    elif cnt <= m:
        end = mid - 1
        result = mid

print(result)