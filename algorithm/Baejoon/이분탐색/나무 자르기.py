n,m = map(int,input().split(" "))
height = list(map(int,input().split(" ")))

start = 0
end = max(height)
ans = 0

def tree_height(h):
    remain = 0
    for i in range(n):
        if height[i] > h:
            remain += (height[i]-h)
    return remain

while start <= end:
    mid = (start+end) // 2
    s = tree_height(mid)
    # print(mid,s)
    if s < m:
        end = mid - 1
    else:
        start = mid + 1

# 3 1
# 10 10 10
print(end)