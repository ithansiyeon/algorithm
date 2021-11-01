n,m,k = map(int,input().split(" "))
nums = list(map(int,input().split(" ")))
nums.sort(reverse=True)
sum = m//(k+1)*(nums[0]*k+nums[1])+(m%(k+1))*nums[0]
print(sum)

result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result+=nums[0]
        m-=1
    if m==0:
        break
    result+=nums[1]
    m-=1
print(result)


