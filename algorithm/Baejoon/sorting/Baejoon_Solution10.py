n = int(input())

nums = input().split(" ")
nums2 = sorted(list(set(nums)))
dic = {nums2[i] : i for i in range(len(nums2))}
for i in nums:
    print(dic[i],end=' ')