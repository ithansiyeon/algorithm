n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
a.sort()
for i in range(m):
    mid = n // 2
    start = 0
    end = n-1
    while start <= end:
        if a[mid] > b[i]:
            end = mid-1
            mid = (start+end) // 2
        elif a[mid] < b[i]:
            start = mid+1
            mid = (start+end) // 2
        else:
            print(1)
            break
    else:
        print(0)