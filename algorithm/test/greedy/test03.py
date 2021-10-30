n = int(input())
scar = list(map(int,input().split(" ")))
scar.sort()
cnt = 0
for i in list(set(scar)):
    if n-i < 0:
        break
    n-=i
    cnt+=1
print(cnt)

result = 0
count = 0
for i in scar:
    count+=1
    if count >= i:
        result += 1
        count = 0
print(result)
