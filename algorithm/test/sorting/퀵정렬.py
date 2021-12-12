array = [5,7,9,0,3,1,6,2,4,8]
# pivot을 정하고 왼쪽에서 부터 큰값과 오른쪽에서 부터는 작은값을 찾아서 스와핑
# 서로 위치가 엇갈리게 되면 작은값을 pivot과 교환함
def quick_sort(left,right,pivot):
    if pivot >= right:
        return
    while left <= right:
        while left<=right and array[left] <= array[pivot]:
            left+=1
        while right>pivot and array[right] >= array[pivot]:
            right-=1
        print(left,right,pivot)
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    print(pivot)
    quick_sort(pivot+1,right-1,pivot) # 왼쪽 분할
    quick_sort(right+2,len(array)-1,right+1) # 오른쪽 분할

quick_sort(1,len(array)-1,0)
print(array)