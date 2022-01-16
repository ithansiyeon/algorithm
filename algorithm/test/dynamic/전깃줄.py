import sys
input = sys.stdin.readline
n = int(input())
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

array.sort()
dp = [1]*n

for i in range(n):
    for j in range(i):
        if array[i][1] > array[j][1]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))

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