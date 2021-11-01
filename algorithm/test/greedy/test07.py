n,k = map(int,input().split(" "))
cnt = 0
while n!=1:
    if n >= k:
        cnt+=(n%k)
        n-=(n%k)
        cnt+=1
        n//=k
    else:
        cnt+=n-1
        n=1
print(cnt)
result = 0
n,k = map(int,input().split(" "))
while True:
    target = (n//k)*k
    result += (n-target)
    n = target
    if n<k:
        break
    result+=1
    n//=k

result+=(n-1)
print(result)

