import sys

n,m = map(int,sys.stdin.readline().rstrip().split(" "))
array = list(map(int,sys.stdin.readline().rstrip().split(" ")))

start = max(array) # 레코드가 가질 수 있는 가장 작은 크기
end = sum(array) # 레슨을 하나의 레코드에 다 담을 수 있을 때

result = 0
# 더 이상 검색할 범위가 없음
while start <= end:
    cnt = 1
    hap = 0
    mid = (start+end) // 2

    for i in range(n):
        if array[i] + hap > mid:
            hap = 0
            cnt += 1
        hap+=array[i]

    # 개수가 많아지므로 블루레이의 크기를 더 크게 해야 됨
    if cnt > m:
        start = mid + 1
    # 개수가 적거가 같으면 블루레이의 크기를 더 작게 함(같을 떄는 가능한 블루레이의 크기 중 최소를 구해야 하므로)
    else:
        end = mid - 1
        result = mid

print(result)
