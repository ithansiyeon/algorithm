n,m = map(int,input().split(" "))
result = 0
row = -1
for i in range(n):
    nums = list(map(int,input().split(" ")))
    result=max(result,min(nums))
print(result)