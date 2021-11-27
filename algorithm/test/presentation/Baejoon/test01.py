n = int(input())
if n%5 == 0:
    print(n//5)
elif (n%5)%3 == 0:
    print(n//5+(n%5)//3)
else:
    cnt = 0
    loop = True
    while n%5 != 0:
        n = n - 3
        cnt+=1
        if n < 0:
            loop = False
            break
    if not loop:
        print(-1)
    else:
        print(cnt+n//5)





