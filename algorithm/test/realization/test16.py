snums = set()
i = 1
while True:
    if i > 10000:
        break
    s = i
    for j in str(s):
        s+=int(j)
    snums.add(s)
    i+=1
nums = list(range(1,10001))

for i in list(sorted(nums-snums)):
    print(i)
