n = int(input())

if n%5 == 0:
    print(n//5)
elif n%5 == 3:
    print(n//5+1)
else:
    m = n
    cnt = 0
    while m:
        if m - 3 >= 0:
            cnt+=1
            m-=3
        else:
            print(-1)
            break
        if m % 5 == 0:
            print(cnt+m//5)
            break



