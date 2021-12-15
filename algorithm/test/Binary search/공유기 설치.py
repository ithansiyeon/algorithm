import sys

n,c = map(int,input().split(" "))
array = []
for i in range(n):
    array.append(int(sys.stdin.readline().rstrip()))

array.sort()
start = 1
end = array[-1] - array[0]

result = 0
while start<=end:
    mid = (start+end) // 2
    current = array[0]
    cnt = 1
    for i in range(1,n):
        if array[i] - current >= mid:
            current = array[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)