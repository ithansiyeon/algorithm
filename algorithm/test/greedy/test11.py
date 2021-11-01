import copy

n = int(input())
money = list(map(int,input().split(" ")))
money.sort(reverse=True)
cnt = 1
while True:
    loop = True
    s = copy.deepcopy(cnt)
    if cnt not in money:
        for i in range(len(money)):
            if s < money[i] or s-money[i] < 0:
                loop = False
                continue
            s-=money[i]
            if s not in money[i+1:]:
                loop = False
            else:
                loop = True
                break
    if not loop:
        print(cnt)
        break
    cnt+=1

money.sort()
target = 1
for x in money:
    if target < x:
        break
    target+=x
print(target)



