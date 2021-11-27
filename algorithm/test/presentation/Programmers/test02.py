n,r,c = map(int,input().split(" "))
cnt = 0
while n:
    size = 2**(n-1)
    if size <= r and size <= c: # 4사분면
        cnt+=size**2*3
        r-=size
        c-=size
    elif size <= r and c < size:  # 3사분면
        cnt+=size**2*2
        r-=size
    elif r < size and c < size: # 2사분면
        pass
    elif r < size and c >= size: # 1사분면
        cnt+=size**2
        c-=size
    n-=1

if r == 0 and c == 0:
    print(cnt)
elif r == 1 and c == 0:
    print(cnt+2)
elif r == 0 and c == 1:
    print(cnt+1)
elif r == 1 and c == 1:
    print(cnt+3)


