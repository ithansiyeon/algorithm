n,m = 4,6
data = [19,15,10,17]
res = 0
start = 1
end = max(data)
res = 0

while start <= end:
    mid = (start+end) // 2
    tot = 0
    for d in data:
        if d > mid:
            tot+=d-mid
    if tot >= m:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)