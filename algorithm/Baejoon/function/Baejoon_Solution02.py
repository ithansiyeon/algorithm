nums = list(range(1,10000))
num_set = set()
for num in nums:
    for n in str(num):
        num+=int(n)
    num_set.add(num)

for i in sorted(set(nums)-num_set):
    print(i)
