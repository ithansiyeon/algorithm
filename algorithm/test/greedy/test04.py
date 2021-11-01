n = int(input())
money = [500,100,50,10]
cnt = 0
for i in money:
    cnt+=n//i
    n=n%i
print(cnt)

