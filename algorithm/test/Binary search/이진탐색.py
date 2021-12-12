def binary_search(data,start,end,target):
    while start <= end:
        mid = (start+end) // 2
        if data[mid] == target:
            return mid
        if target > data[mid]:
            start = mid + 1
        if target < data[mid]:
            end = mid - 1
    return None
data = [1,2,3,6,7,8,9]
result = binary_search(data,0,len(data)-1,4)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
