n=5
nlist = [8,3,7,9,2]
m = 3
mlist = [5,7,9]

def find(target,start,end):
    while start <= end:
        mid = (start+end)//2
        if nlist[mid] == target:
            return mid
        elif nlist[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

for i in mlist:
    start = 0
    end = n-1
    if find(i,start,end):
        print("yes",end=" ")
    else:
        print("no",end=" ")