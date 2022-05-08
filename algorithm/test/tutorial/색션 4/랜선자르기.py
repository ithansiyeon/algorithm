import sys
sys.stdin = open("in5.txt", "rt")
k, n = map(int,input().split())
nlist = []
for i in range(k):
    nlist.append(int(input()))

end = max(nlist)
start = 1

while start < end:
    cnt = 0
    mid = (start+end) // 2
    for i in range(k):
        cnt += nlist[i] // mid
    if cnt >= n:
        start = mid + 1
    else:
         end = mid
    if start > end:
        break

print(mid)