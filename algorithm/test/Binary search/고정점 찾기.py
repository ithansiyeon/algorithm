n = int(input())
array = list(map(int,input().split(" ")))
# 값이 현재값하고 가야 되는데 만약에 다르면 인덱스가 더 크니까 오른쪽이고 그 아래로는 값이 작을거니까
# 인덱스가 만약에 더 작으면 아래로 가야 되고
def binary_search_left(array,start,end):
    while start <= end:
        mid = (start+end) // 2
        if mid == array[mid]:
            return mid
        elif mid < array[mid]:
            end = mid-1
        else:
            start = mid + 1
    return None

result = binary_search_left(array,0,n-1)

if result == None:
    print(-1)
else:
    print(result)

