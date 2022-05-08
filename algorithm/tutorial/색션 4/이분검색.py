import sys
sys.stdin = open("in5.txt", "rt")
n, m = map(int,input().split())
nlist = list(map(int,input().split()))
nlist.sort()
start = 0
end = n
mid = (start+end) // 2
while True:
    if m > nlist[mid]:
        start = mid
    elif m == nlist[mid]:
        break
    else:
        end = mid
    mid = (start+end) // 2

print(mid+1)
