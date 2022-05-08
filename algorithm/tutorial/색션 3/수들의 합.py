import sys
sys.stdin = open("in5.txt", "rt")
n,m = map(int,input().split())

nlist = list(map(int,input().split()))

lt = 0
rt = 1
cnt = 0
hap = nlist[0]
while True:
    if rt >= n and hap < m:
        break
    if hap < m:
        hap += nlist[rt]
        rt += 1
    elif hap == m:
        cnt+=1
        hap -= nlist[lt]
        lt+=1
    else:
        hap -= nlist[lt]
        lt += 1

print(cnt)


