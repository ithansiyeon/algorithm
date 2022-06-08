import sys
sys.stdin = open("in5.txt", "rt")
n, m = map(int,input().split())
nlist = list(map(int,input().split()))

start = max(nlist)
end = sum(nlist)
res = 0
maxx = max(nlist)

while start <= end:
    mid = (start+end)//2
    hap = 0
    cnt = 1
    for x in nlist:
        if hap + x > mid:
            cnt+=1
            hap = x
        else:
            hap+=x

    if cnt <= m and mid >= maxx:
        res = mid
        end = mid - 1
    else:
        start = mid + 1

print(res)

