import sys
input = sys.stdin.readline
k,n = map(int,input().split(" "))

line = []
for i in range(k):
    line.append(int(input()))

sizeMax = 0
start = 1
end = max(line)
cnt = 0
line.sort()
def fn_size(w):
    cnt1 = 0
    for i in line:
        cnt1+=(i//w)
    return cnt1

while start <= end:
    mid = (start+end) // 2
    cnt = fn_size(mid)
    if cnt < n:
        end = mid - 1
    else:
        start = mid + 1
        sizeMax = max(sizeMax,mid)

print(sizeMax)

