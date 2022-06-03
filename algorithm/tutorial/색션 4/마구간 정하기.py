import sys
sys.stdin = open("in5.txt", "rt")
n,c = map(int,input().split())
data = [int(input()) for _ in range(n)]
data.sort()
start = data[0]
end = data[-1]
res = 0

def count(mid):
    cnt = 1
    dis = data[0]
    for i in range(1,n):
        if data[i]-dis >= mid:
            dis = data[i]
            cnt+=1
    return cnt

while start<=end:
    mid = (start+end)//2
    if count(mid) >= c:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)

