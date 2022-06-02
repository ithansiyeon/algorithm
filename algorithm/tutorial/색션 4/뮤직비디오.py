import sys
sys.stdin = open("in5.txt", "rt")
n, m = map(int,input().split())
nlist = list(map(int,input().split()))

start = 1
end = sum(nlist)
res = 0
maxx = max(nlist)

while True:
    mid = (start+end)//2
    sum = 0
    cnt = 1
    for x in nlist:
        if sum + x > mid:
            cnt+=1
            sum = x
        else:
            sum+=x

    if cnt <= m and mid >= maxx:
        res = mid
        end = mid - 1
    else:
        start = mid + 1

    if start > end:
        break
print(res)

