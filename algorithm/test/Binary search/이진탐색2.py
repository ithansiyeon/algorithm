def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    elif target > array[mid]:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)


array = [1,3,4,6,7,8,9,13]

result = binary_search(array,3,0,len(array)-1)
if result == None:
    print("해당 원소가 존재하지 않습니다.")
else:
    print(result)