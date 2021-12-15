def merge_sort(data):
    return split(data)

def split(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    print(mid)
    left = split(data[:mid])
    right = split(data[mid:])
    print("split: {0} {1}".format(left,right))
    return merge(left,right)

def merge(left,right):
    print("merge: {0} {1}".format(left, right))
    temp = []
    l, h = 0,0
    # case 1: left/right가 아직 남아있을 때
    while l < len(left) and h < len(right):
        if left[l] > right[h]:
            temp.append(right[h])
            h+=1
        else:
            temp.append(left[l])
            l+=1

    # case 2: left만 남아있을 때
    while l < len(left):
        temp.append(left[l])
        l+=1

    # case 3: right만 남아있을 때
    while h < len(right):
        temp.append(right[h])
        h+=1
    print("합병: {0}: ".format(temp))
    print()
    return temp




if __name__ == '__main__':
    data = [6, 5, 3, 1, 8, 7, 2, 4]
    print(merge_sort(data))

