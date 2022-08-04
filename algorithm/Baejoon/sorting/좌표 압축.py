n = int(input())

nums = list(map(int,input().split(" ")))
nums2 = sorted(list(set(nums)))
dic = {nums2[i] : i for i in range(len(nums2))}
for i in nums:
    print(dic[i],end=' ')