n = int(input())
plist = list(map(int,input().split(" ")))
plist.sort()
sum1 = 0
for i in range(0,n):
    sum1+=sum(plist[:i+1])
print(sum1)