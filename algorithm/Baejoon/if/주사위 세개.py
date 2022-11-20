from collections import Counter

nums = Counter(list(map(int,input().split(" "))))

if len(nums) == 1:
    print(10000+nums.most_common(1)[0][0]*1000)
elif len(nums) == 2:
    print(1000+nums.most_common(1)[0][0]*100)
else:
    print(max(nums)*100)



