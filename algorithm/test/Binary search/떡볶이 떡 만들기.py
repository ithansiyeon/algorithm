# 조건의 만족 여부에 따라서 탐색 범위를 좁혀서 해결
n, m = map(int,input().split(" "))

rice_height = list(map(int,input().split(" ")))

height = [i for i in range(0,max(rice_height))]
start,end = 0, len(height)-1

while start <= end:
    hap = 0
    cnt = 0
    mid = (start + end) // 2
    for i in range(n):
        if rice_height[i] > height[mid]:
            hap+=rice_height[i]
            cnt+=1

    val = hap - height[mid]*cnt
    if m < val:
        start = mid + 1
    else:
        result = height[mid]
        end = mid - 1

print(result)

